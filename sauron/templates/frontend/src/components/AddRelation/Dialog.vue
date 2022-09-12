<template>
  <div class="absolute bottom-0 right-0 mb-8">
    <Button icon="pi pi-plus" class="p-button-rounded p-button-info m-4"
            @click="addDialogOpened = true"/>
  </div>

  <Dialog :header="$t('misc.add_relation')" v-model:visible="addDialogOpened"
          class="h-full w-full m-5"
          :modal="true" content-class="flex-1">
    <form class="p-fluid formgrid grid">

    </form>
    <template #footer>
    </template>
  </Dialog>

  <TagEdit v-if="tagEditDialogOpened"/>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

// eslint-disable-next-line import/no-unresolved
import TagEdit from '@/components/TagEdit.vue';

export default {
  components: {
    TagEdit,
  },

  data() {
    return {
      addDialogOpened: true,
      tagEditDialogOpened: true,
      form: {
        firstName: '',
        lastName: '',
        tags: [],
        links: [],
        note: '',
        nicknames: '',
      },
      tags: [],
    };
  },
  computed: {
    ...mapGetters(['StateTags']),
  },
  methods: {
    ...mapActions(['GetTags', 'CreateRelation']),
  },
  async created() {
    if (this.StateTags.length === 0) await this.GetTags();
    this.tags = this.StateTags;
  },
};
</script>
