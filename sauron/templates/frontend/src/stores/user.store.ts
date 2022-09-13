import { User } from '@/models/user.model';
import { defineStore } from 'pinia';
import axios from 'axios';
import { UserAPIResponse, UserLoginForm, UserRegisterForm } from '@/types/user';

interface State {
  key: string | null,
  user: User | null,
}

const useUserStore = defineStore({
  id: 'userStore',
  state: (): State => ({
    key: null,
    user: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
  },

  actions: {
    async Register(form: UserRegisterForm) {
      await axios.post('/api/accounts/registration/', form);
    },

    async LogIn(form: UserLoginForm) {
      const req = await axios.post('/api/accounts/login/', form);
      this.setKey(req.data.key);

      this.setUser(
        (await axios.get(
          '/api/users/me/',
          {
            headers: {
              Authorization: `token ${this.key}`,
            },
          },
        )).data,
      );
    },

    async LogOut() {
      await axios.post('/api/accounts/logout/');
      this.$reset();
    },

    async UpdateUser(form: User) {
      const data = {
        first_name: form.firstName,
        last_name: form.lastName,
        language: form.language,
        theme: form.theme?.code,
        avatar: form.avatar,
      };

      this.setUser(await axios.patch('/api/accounts/user/', data));
    },

    setKey(key: string) {
      this.key = key;
    },

    setUser(payload: UserAPIResponse) {
      this.user = {
        username: payload.username,
        firstName: payload.first_name,
        lastName: payload.last_name,
        avatar: payload.avatar,
        theme: {
          code: payload.theme,
        },
        language: payload.language,
      };
    },
  },
  persist: true,
});

export default useUserStore;
