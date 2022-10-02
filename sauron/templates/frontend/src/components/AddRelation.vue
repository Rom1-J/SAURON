<script lang="ts" setup>
import { useTagStore } from '@/stores';
import { ref } from 'vue';

const tagStore = useTagStore();

const addDialogOpened = ref(false);
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
    <form>
      <div class="flex">
        <p>
          {{ tagStore.tags }}
        </p>

        <Divider layout="vertical" />

        <p>
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem
          accusantium doloremque laudantium, totam rem aperiam, eaque ipsa
          quae ab illo inventore veritatis et quasi architecto beatae vitae
          dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
          aspernatur aut odit aut fugit, sed quia consequuntur magni dolores
          eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci
          velit, sed quia non numquam eius modi.
        </p>

        <Divider layout="vertical" />

        <p>
          Sed ut perspiciatis unde omnis iste natus error sit voluptatem
          accusantium doloremque laudantium, totam rem aperiam, eaque ipsa
          quae ab illo inventore veritatis et quasi architecto beatae vitae
          dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit
          aspernatur aut odit aut fugit, sed quia consequuntur magni dolores
          eos qui ratione voluptatem sequi nesciunt. Consectetur, adipisci
          velit, sed quia non numquam eius modi.
        </p>
      </div>
    </form>
    <template #footer>
      dza
    </template>
  </Dialog>
</template>
