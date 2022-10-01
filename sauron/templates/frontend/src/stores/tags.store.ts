import { Tag } from '@/models/tag.model';
import { defineStore } from 'pinia';
import axios from 'axios';

interface State {
  tags: Tag[],
}

const useTagStore = defineStore({
  id: 'tagStore',
  state: (): State => ({
    tags: [],
  }),

  actions: {
    async RegisterTag(form: Tag): Promise<Tag[]> {
      await axios.post('/api/tags/', form);
      await this.FetchTags();
      return this.tags;
    },

    async DeleteTag(id: string): Promise<Tag[]> {
      await axios.delete(`/api/tags/${id}`);
      await this.FetchTags();
      return this.tags;
    },

    async FetchTags(): Promise<Tag[]> {
      this.setTags((await axios.get('/api/tags/')).data);
      return this.tags;
    },

    async GetTags(): Promise<Tag[]> {
      return this.tags || await this.FetchTags();
    },

    setTags(data: Tag[]) {
      this.tags = data;
    },
  },
});

export default useTagStore;
