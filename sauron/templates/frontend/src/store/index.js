import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import auth from './modules/auth';
import tags from './modules/tags';

// Create store
export default new Vuex.Store({
  modules: {
    auth,
    tags,
  },
  plugins: [createPersistedState()],
});
