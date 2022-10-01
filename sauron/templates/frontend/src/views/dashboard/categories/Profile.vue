<script lang="ts" setup>
import { reactive, ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { useToast } from 'primevue/usetoast';
import { useConfirm } from 'primevue/useconfirm';
import { useTagStore, useUserStore } from '@/stores';
import axios, { AxiosError } from 'axios';
import { ServerError } from '@/types/server';
// eslint-disable-next-line import/no-unresolved
import RelationTag from '@/components/RelationTag.vue';
// eslint-disable-next-line import/no-unresolved
import EditRelationTag from '@/components/EditRelationTag.vue';

const userStore = useUserStore();
const tagStore = useTagStore();
const toast = useToast();
const confirm = useConfirm();
const { t } = useI18n();

const avatarUrl = ref(userStore.user?.avatar);
const createTagDialog = ref();
const editTagDialog = ref({});

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

async function handleSubmit() {
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

function createTag() {
  createTagDialog.value.open();
}
function editTag(id: number) {
  console.log(editTagDialog.value);
  editTagDialog.value[id].open();
}

function confirmDelete(event: PointerEvent, id: string) {
  confirm.require({
    target: event.currentTarget as HTMLElement | undefined,
    message: t('action.delete_entry'),
    icon: 'pi pi-info-circle',
    acceptClass: 'p-button-danger',
    accept: async () => {
      await tagStore.DeleteTag(id);
      toast.add({
        severity: 'info',
        summary: t('status.disconnection.title'),
        detail: t('status.tag_deleted'),
        life: 5000,
      });
    },
  });
}

const init = async () => {
  await tagStore.FetchTags();
};

init();
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
          @submit.prevent="handleSubmit()"
          class="p-fluid formgrid grid">
          <div class="field col-12 md:col-6">
            <label for="firstname">
              {{ $t('fields.firstname') }}
            </label>
            <InputText
              v-model="state.firstName"
              id="firstname"
              type="text" />
          </div>
          <div class="field col-12 md:col-6">
            <label for="lastname">
              {{ $t('fields.lastname') }}
            </label>
            <InputText
              v-model="state.lastName"
              id="lastname"
              type="text" />
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
            <Button :label="$t('status.save')" type="submit" />
          </div>
        </form>
      </div>
    </div>

    <div class="col-12">
      <div class="card">
        <div class="grid">
          <div class="col-6 mb-4">
            <span class="text-2xl mr-1">{{ $t('fields.tags') }}</span>
            <i class="text-sm">({{ tagStore.tags.length }})</i>
          </div>
          <div class="col-6 flex justify-content-end">
            <Button class="p-button-success" @click="createTag" icon="pi pi-plus" />
            <EditRelationTag ref="createTagDialog" />
          </div>
        </div>

        <DataTable
          :value="tagStore.tags"
          :loading="!tagStore.tags"
          class="mt-3">
          <Column>
            <template #body="{ data }">
              <RelationTag :tag="data" />
            </template>
          </Column>
          <Column field="note" :header="$t('fields.tags.note')" />
          <Column field="uses" :header="$t('fields.tags.uses')" />
          <Column class="text-right">
            <template #body="{ data }">
              <span class="p-buttonset">
                <Button
                  icon="pi pi-pencil"
                  class="p-button-info"
                  @click="editTag(data.id)"
                />
                <Button
                  @click="confirmDelete($event, data.id)"
                  icon="pi pi-trash"
                  class="p-button-danger" />
                <ConfirmPopup />
                <EditRelationTag :ref="`editTagDialog_${data.id}`" :tag="data" />
              </span>
            </template>
          </Column>
          <template #empty>
            {{ t('fields.tags.empty') }}
          </template>
        </DataTable>
      </div>
    </div>
  </div>
</template>
