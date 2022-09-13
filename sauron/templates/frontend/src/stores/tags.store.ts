import { Tag } from '@/models/tag.model';
import { defineStore } from 'pinia';
import axios from 'axios';

import useUserStore from '@/stores/user.store';

interface State {
  tags: Tag[],
}

const useTagStore = defineStore({
  id: 'tagStore',
  state: (): State => ({
    tags: [],
  }),

  actions: {
    async RegisterTag(form: Tag) {
      console.log(form);
    },

    async GetTags() {
      this.setTags(
        (await axios.get(
          '/api/tags/',
          {
            headers: {
              Authorization: `token ${useUserStore().key}`,
            },
          },
        )).data,
      );
    },

    setTags(data: Tag[]) {
      this.tags = data;
    },
  },
});

export default useTagStore;
