<script lang="ts" setup>
import { required } from '@vuelidate/validators';

// eslint-disable-next-line import/no-unresolved
import RelationTag from '@/components/RelationTag.vue';
import { reactive, ref } from 'vue';
import { useToast } from 'primevue/usetoast';
import { useI18n } from 'vue-i18n';
import { useTagStore } from '@/stores';
import { useVuelidate } from '@vuelidate/core';
import axios, { AxiosError } from 'axios';
import { ServerError } from '@/types/server';

const tagStore = useTagStore();
const toast = useToast();
const { t } = useI18n();

const submitted = ref(false);
const dialogOpened = ref(false);

const state = reactive({
  name: '',
  color: '',
  note: '',
});

const rules = {
  name: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

async function handleSubmit(isFormValid: boolean) {
  if (!isFormValid) return;
  submitted.value = true;

  try {
    await tagStore.RegisterTag(state);
    toast.add({
      severity: 'info',
      summary: t('status.confirmation'),
      detail: t('tag.success_creation'),
      life: 5000,
    });
    await tagStore.GetTags();
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
      } else {
        toast.add({
          severity: 'error',
          summary: t('status.error.title'),
          detail: t('status.error.unknown'),
          life: 5000,
        });
      }
    }
  }

  submitted.value = false;
}
</script>

<template>
  <Dialog
    :header="$t('misc.edit_tag')"
    v-model:visible="dialogOpened"
    :modal="true"
    content-class="flex-1">
    <template #header>
      <span class="p-dialog-title">
        {{ $t('misc.edit_tag') }}
      </span>
      <RelationTag v-if="state.name" :name="state.name" :color="state.color" :note="state.note" />
    </template>

    <form class="p-fluid formgrid grid">
      <div class="field col-10">
        <label
          for="name"
          :class="{ 'p-error': v$.name.$invalid && v$.name.$model }">
          {{ $t('fields.name') }}
        </label>

        <InputText
          v-model="v$.form.name.$model"
          id="name"
          type="text"
          class="p-inputtext-sm"
          :class="{ 'p-invalid': v$.name.$invalid && v$.name.$model }" />
      </div>

      <div class="field col-2">
        <label for="color">
          {{ $t('fields.color') }}
        </label>

        <ColorPicker v-model="state.color" id="color" default-color="000000" />
      </div>

      <div class="field col-12">
        <label for="note">
          {{ $t('fields.note') }}
        </label>

        <Textarea :autoResize="true" id="note" rows="3" cols="30" v-model="state.note" />
      </div>
    </form>

    <template #footer>
      <Button
        :label="$t('fields.save_edit')"
        icon="pi pi-check"
        @click="handleSubmit(!v$.$invalid)"
        class="p-button-success"
        iconPos="right"
        :disabled="v$.$invalid || submitted" />
    </template>
  </Dialog>
</template>
