import { Tag } from '@/models/tag.model';
import { defineStore } from 'pinia';
import axios from 'axios';
import { TagCreationForm, TagUpdateForm } from '@/types/tag';

interface State {
  tags: Tag[],
}

const useTagStore = defineStore({
  id: 'tagStore',
  state: (): State => ({
    tags: [],
  }),

  actions: {
    async RegisterTag(form: TagCreationForm): Promise<Tag[]> {
      await axios.post('/api/tags/', form);
      await this.FetchTags();
      return this.tags;
    },

    async UpdateTag(form: TagUpdateForm): Promise<Tag[]> {
      await axios.patch(`/api/tags/${form.id}`, form);
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
      return this.tags.length ? this.tags : this.FetchTags();
    },

    setTags(data: Tag[]) {
      this.tags = data;
    },
  },
  persist: true,
});

export default useTagStore;
