<script lang="ts" setup>
import { useVuelidate } from '@vuelidate/core';
import { maxLength } from '@vuelidate/validators';
import { reactive, ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { useToast } from 'primevue/usetoast';
import { useUserStore } from '@/stores';
import axios, { AxiosError } from 'axios';
import { ServerError } from '@/types/server';

const userStore = useUserStore();
const toast = useToast();
const { t } = useI18n();

const submitted = ref(false);
const avatarUrl = ref(userStore.user?.avatar);

const languageOptions = [
  { name: 'Francais', code: 'fr' },
  { name: 'English', code: 'en' },
];
const themeOptions = [
  { name: t('fields.theme.dark'), code: 'DK' },
  { name: t('fields.theme.light'), code: 'LT' },
];

const state = reactive({
  firstName: userStore.user?.firstName,
  lastName: userStore.user?.lastName,
  language: userStore.user?.language,
  theme: userStore.user?.theme,
  avatar: '',
});

const rules = {
  firstName: {
    maxLengthValue: maxLength(150),
  },
  lastName: {
    maxLengthValue: maxLength(150),
  },
};

const v$ = useVuelidate(rules, state);

async function handleSubmit(isFormValid: boolean) {
  if (!isFormValid) return;
  submitted.value = true;

  try {
    await userStore.UpdateUser(state);
    toast.add({
      severity: 'success',
      summary: t('status.saved.title'),
      detail: t('status.saved.message'),
      life: 5000,
    });
    state.avatar = '';
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const serverError = error as AxiosError<ServerError>;

      if (serverError && serverError.response) {
        Object.values(serverError.response.data).forEach((errors) => {
          const iter = Array.isArray(errors) ? errors : [errors];

          iter.forEach((message) => {
            toast.add({
              severity: 'error',
              summary: t('status.error.title'),
              detail: message,
              life: 5000,
            });
          });
        });
      }
    }
  }

  submitted.value = false;
}

type UploaderEvent = {
  files: File[]
};
function uploader(event: UploaderEvent) {
  const file = event.files[0];

  // @ts-ignore
  state.avatar = new File([file], file.name);
  avatarUrl.value = URL.createObjectURL(file);
}
</script>

<template>
  <div class="grid">
    <div class="col-12">
      <div class="card">
        <div class="grid">
          <div class="col-6 mb-4">
            <span class="text-2xl mr-1">{{ userStore.user?.username }}</span>
            <i class="text-sm">({{ userStore.user?.email }})</i>
          </div>
          <div class="col-6 flex justify-content-end">
            <AvatarGroup v-if="state.avatar">
              <Avatar :image="userStore.user?.avatar" shape="circle" />
              <Avatar v-if="avatarUrl" :image="avatarUrl" shape="circle" size="large" />
            </AvatarGroup>

            <Avatar v-else-if="avatarUrl" :image="avatarUrl" size="large" shape="circle" />
          </div>
        </div>
        <form
          @submit.prevent="handleSubmit(!v$.$invalid)"
          class="p-fluid formgrid grid">
          <div class="field col-12 md:col-6">
            <label
              for="firstname"
              :class="{ 'p-error': v$.firstName.$invalid && v$.firstName.$model }">
              {{ $t('fields.firstname') }}
            </label>
            <InputText
              v-model="v$.firstName.$model"
              id="firstname"
              :class="{ 'p-invalid': v$.firstName.$invalid && v$.firstName.$model }"
              type="text" />
            <small
              v-if="(v$.firstName.$invalid && v$.firstName.$model)
                || v$.firstName.$pending.$response"
              class="p-error">
              {{ v$.firstName.maxLengthValue.$message }}
            </small>
          </div>
          <div class="field col-12 md:col-6">
            <label
              for="lastname"
              :class="{ 'p-error': v$.lastName.$invalid && v$.lastName.$model }">
              {{ $t('fields.lastname') }}
            </label>
            <InputText
              v-model="v$.lastName.$model"
              id="lastname"
              :class="{ 'p-invalid': v$.lastName.$invalid && v$.lastName.$model }"
              type="text" />
            <small
              v-if="(v$.lastName.$invalid && v$.lastName.$model)
                || v$.lastName.$pending.$response"
              class="p-error">
              {{ v$.lastName.maxLengthValue.$message }}
            </small>
          </div>
          <div class="field col-12 md:col-4">
            <label for="language">
              {{ $t('fields.language') }}
            </label>
            <Dropdown
              v-model="state.language"
              :options="languageOptions"
              optionLabel="name"
              option-value="code"
              id="language" />
          </div>

          <div class="field col-12 md:col-4">
            <label for="theme">
              {{ $t('fields.theme.title') }}
            </label>
            <Dropdown
              v-model="state.theme"
              :options="themeOptions"
              optionLabel="name"
              option-value="code"
              id="theme" />
          </div>

          <div class="field col-12 md:col-4">
            <label for="avatar">
              {{ $t('fields.avatar') }}
            </label>
            <FileUpload
              mode="basic"
              v-model="state.avatar"
              class="w-full"
              :choose-label="$t('fields.choose')"
              name="avatar"
              accept="image/*"
              custom-upload
              @uploader="uploader"
              auto
              :maxFileSize="1000000" />
          </div>

          <div class="field col-12 mt-5">
            <Button :label="$t('status.save')" :disabled="submitted || v$.$invalid" type="submit" />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>