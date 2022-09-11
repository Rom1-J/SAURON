import axios from 'axios';

export default {
  state: {
    tags: [],
  },
  getters: {
    StateTags: (state) => state.tags,
  },
  actions: {
    async GetTags({ commit, getters }) {
      await commit(
        'setTags',
        (await axios.get(
          '/api/tags/',
          {
            headers: {
              Authorization: `token ${getters.StateKey}`,
            },
          },
        )).data,
      );
    },
  },
  mutations: {
    setTags(state, data) {
      state.tags = data;
    },
  },
};
