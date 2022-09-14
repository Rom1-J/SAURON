import { User } from '@/models/user.model';
import { defineStore } from 'pinia';
import axios from 'axios';
import {
  UserAPIResponse, UserLoginForm, UserRegisterForm, UserUpdateForm,
} from '@/types/user';

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

      await this.GetUser();
    },

    async LogOut() {
      await axios.post('/api/accounts/logout/');
      this.$reset();
    },

    async GetUser() {
      this.setUser((await axios.get('/api/users/me/')).data);
    },

    async UpdateUser(form: User) {
      const data: UserUpdateForm = {
        first_name: form.firstName,
        last_name: form.lastName,
        language: form.language,
        theme: form.theme,
      };

      // @ts-ignore
      if (form.avatar instanceof Blob) data.avatar = form.avatar;

      await axios.put(
        this.user?.url || '/api/accounts/user/',
        data,
        {
          headers: {
            'content-type': 'multipart/form-data',
          },
        },
      );
      await this.GetUser();
    },

    setKey(key: string) {
      this.key = key;
    },

    setUser(payload: UserAPIResponse) {
      this.user = {
        username: payload.username,
        email: payload.email,
        firstName: payload.first_name,
        lastName: payload.last_name,
        avatar: payload.avatar,
        theme: payload.theme,
        language: payload.language,
        url: payload.url,
      };
    },
  },
  persist: true,
});

export default useUserStore;
