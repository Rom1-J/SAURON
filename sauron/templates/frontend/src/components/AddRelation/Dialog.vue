<script lang="ts" setup>
// eslint-disable-next-line import/no-unresolved
import TagEdit from '@/components/TagEdit.vue';
import { useTagStore } from '@/stores';
import { ref } from 'vue';
import { Tag } from '@/models/tag.model';

const tagStore = useTagStore();

const addDialogOpened = ref(false);
const tagEditDialogOpened = ref(false);

let tags: Tag[] = [];
console.log(tags);

const init = async () => {
  if (tagStore.tags.length === 0) await tagStore.GetTags();
  tags = tagStore.tags;
};

init();
</script>

<template>
  <div class="absolute bottom-0 right-0 mb-8">
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
    <form class="p-fluid formgrid grid" />
    <template #footer />
  </Dialog>

  <TagEdit v-if="tagEditDialogOpened" />
</template>
