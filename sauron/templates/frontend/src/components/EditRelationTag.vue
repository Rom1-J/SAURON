<script lang="ts" setup>
import { required } from '@vuelidate/validators';

// eslint-disable-next-line import/no-unresolved
import RelationTag from '@/components/RelationTag.vue';
import { reactive, ref, toRef } from 'vue';
import { useToast } from 'primevue/usetoast';
import { useI18n } from 'vue-i18n';
import { useVuelidate } from '@vuelidate/core';
import { useTagStore } from '@/stores';
import axios, { AxiosError } from 'axios';
import { ServerError } from '@/types/server';
import { TagUpdateForm } from '@/types/tag';
import { Tag } from '@/models/tag.model';

const tagStore = useTagStore();
const toast = useToast();
const { t } = useI18n();

const submitted = ref(false);
const opened = ref(false);

const props = withDefaults(defineProps<{
  tag?: TagUpdateForm
  edit?: boolean
}>(), {
  tag: () => ({
    id: '',
    name: '',
    note: '',
    color: '000000',
  }),
  edit: false,
});

const edit = toRef(props, 'edit');
const tagData = toRef(props, 'tag');

const state = reactive({
  name: tagData.value?.name,
  color: tagData.value?.color,
  note: tagData.value?.note,
}) as Tag;

const rules = {
  name: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

function fillData(tag: Tag) {
  state.id = tag.id;
  state.name = tag.name;
  state.note = tag.note;
  state.color = tag.color;
}
function open() {
  opened.value = true;
}
function close() {
  opened.value = false;
}

defineExpose({
  fillData, open, close,
});

async function handleSubmit(isFormValid: boolean) {
  if (!isFormValid) return;
  submitted.value = true;

  try {
    if (edit.value && props.tag) {
      await tagStore.UpdateTag({ ...state, id: props.tag.id });
    } else {
      await tagStore.RegisterTag(state);
    }
    toast.add({
      severity: 'info',
      summary: t('status.confirmation'),
      detail: edit.value ? t('tag.success_edition') : t('tag.success_creation'),
      life: 5000,
    });

    await tagStore.FetchTags();

    state.name = '';
    state.note = '';
    state.color = '';

    close();
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
    v-model:visible="opened"
    :modal="true"
    :draggable="false"
    content-class="flex-1">
    <template #header>
      <span class="p-dialog-title">
        {{ edit ? $t('misc.edit_tag') : $t('misc.add_tag') }}
      </span>
      <RelationTag v-if="state.name" :name="state.name" :note="state.note" :color="state.color" />
    </template>

    <form class="p-fluid formgrid grid">
      <div class="field col-10">
        <label
          for="name"
          :class="{ 'p-error': v$.name.$invalid && v$.name.$model }">
          {{ $t('fields.name') }}
        </label>

        <InputText
          v-model="v$.name.$model"
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
        :label="edit ? $t('fields.save') : $t('fields.create')"
        icon="pi pi-check"
        @click="handleSubmit(!v$.$invalid)"
        class="p-button-success"
        iconPos="right"
        :disabled="v$.$invalid || submitted" />
    </template>
  </Dialog>
</template>
