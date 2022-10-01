<script lang="ts" setup>
// eslint-disable-next-line import/no-unresolved
import EditRelationTag from '@/components/EditRelationTag.vue';
import { useTagStore } from '@/stores';
import { ref } from 'vue';
import { Tag } from '@/models/tag.model';

const tagStore = useTagStore();

const addDialogOpened = ref(false);
const editTagDialogOpened = ref(false);

let tags: Tag[] = [];

const init = async () => {
  tags = await tagStore.FetchTags();
};

init();
</script>

<template>
  <div class="fixed bottom-0 right-0 mb-8">
    <Button
      icon="pi pi-plus"
      class="p-button-rounded p-button-info m-4"
      @click="addDialogOpened = true" />
  </div>

  <Dialog
    :header="$t('misc.add_relation')"
    v-model:visible="addDialogOpened"
    class="h-full w-full m-5"
    :modal="true"
    content-class="flex-1">
    <form class="p-fluid formgrid grid">
      {{ tags }}
    </form>
    <template #footer>
      dza
    </template>
  </Dialog>

  <EditRelationTag v-if="editTagDialogOpened" />
</template>
