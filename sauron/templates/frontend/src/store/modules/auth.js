import axios from 'axios';

export default {
  state: {
    key: null,
    user: null,
  },
  getters: {
    isAuthenticated: (state) => !!state.user,
    StateUser: (state) => state.user,
    StateKey: (state) => state.key,
  },
  actions: {
    async LogIn({ commit, getters }, form) {
      const req = await axios.post('/api/accounts/login/', form);
      await commit('setKey', req.data.key);

      await commit(
        'setUser',
        (await axios.get(
          '/api/users/me/',
          {
            headers: {
              Authorization: `token ${getters.StateKey}`,
            },
          },
        )).data,
      );
    },

    async LogOut({ commit }) {
      await axios.post('/api/accounts/logout/');
      commit('logout');
    },

    async UpdateUser({ commit, getters }, form) {
      const data = {
        first_name: form.firstName,
        last_name: form.lastName,
        language: form.language,
        theme: form.theme.code,
        avatar: form.avatar,
      };

      await axios.patch('/api/accounts/user/', data);
      await commit('setUser', { ...getters.StateUser, ...data });
    },
  },
  mutations: {
    setKey(state, key) {
      state.key = key;
    },
    setUser(state, data) {
      state.user = data;
    },
    logout(state) {
      state.key = null;
      state.user = null;
    },
  },
};
