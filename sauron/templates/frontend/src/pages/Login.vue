<template>
  <div
      class="surface-0 flex align-items-center justify-content-center
       min-h-screen min-w-screen overflow-hidden">
    <div class="grid justify-content-center p-2 lg:p-0" style="min-width:80%">
      <div class="col-12 mt-5 xl:mt-0 text-center">
        <router-link :to="{name: 'landing'}"
                     class="hover:underline">
          <img src="@/layout/images/logo.svg" alt="SAURON logo" class="mb-5"
               height="64">
        </router-link>
      </div>
      <div class="col-12 xl:col-6"
           style="border-radius:56px; padding:0.3rem;
           background: linear-gradient(180deg, var(--primary-color), rgba(33, 150, 243, 0) 30%);">
        <div class="h-full w-full m-0 py-7 px-4"
             style="border-radius:53px;
             background: linear-gradient(180deg, var(--surface-50) 38.9%, var(--surface-0));">
          <div class="text-center mb-5">
            <div class="text-900 text-3xl font-medium">
              {{ $t('login.sign_in') }}
            </div>
            <span class="text-600 font-medium">
              {{ $t('login.not_registered') }}
              <router-link :to="{name: 'register'}"
                           class="hover:underline">
                {{ $t('register.sign_up') }}
              </router-link>
            </span>
          </div>

          <form @submit.prevent="handleSubmit(!v$.$invalid)"
                class="w-full md:w-10 mx-auto">
            <div class="field">
              <label for="username"
                     :class="{'p-error':v$.username.$invalid && submitted}"
                     class="block text-900 text-xl font-medium mb-2">
                {{ $t('fields.email_or_username') }}
              </label>
              <InputText id="username" v-model="v$.username.$model"
                         :class="{'p-invalid':v$.username.$invalid && submitted}"
                         class="w-full"
                         :placeholder="$t('fields.email_or_username')"
                         style="padding:1rem;"/>
              <ul class="p-0 mt-0 list-none"
                  v-if="(v$.username.$invalid && submitted) || v$.username.$pending.$response">
                <li v-if="v$.username.required.$invalid" class="p-error">
                  {{ v$.username.required.$message }}
                </li>
              </ul>
            </div>

            <div class="field">
              <label for="password"
                     :class="{'p-error':v$.password.$invalid && submitted}"
                     class="block text-900 font-medium text-xl mb-2">
                {{ $t('fields.password') }}
              </label>
              <Password id="password" v-model="v$.password.$model"
                        :placeholder="$t('fields.password')"
                        :class="{'p-invalid':v$.password.$invalid && submitted}"
                        toggleMask :feedback="false" class="w-full"
                        inputClass="w-full"
                        inputStyle="padding:1rem">
              </Password>
              <ul class="p-0 mt-0 list-none"
                  v-if="(v$.password.$invalid && submitted) || v$.password.$pending.$response">
                <li v-if="v$.password.required.$invalid" class="p-error">
                  {{ v$.password.required.$message }}
                </li>
              </ul>
            </div>

            <div class="flex align-items-center justify-content-between mb-5">
              <a class="font-medium no-underline ml-2 text-right cursor-pointer hover:underline">
                {{ $t('fields.forgot_password') }}
              </a>
            </div>
            <Button type="submit" label="Sign In"
                    class="w-full p-3 text-xl" :disabled="submitted || v$.$invalid"></Button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useVuelidate } from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { mapActions } from 'vuex';

export default {
  setup() {
    return { v$: useVuelidate() };
  },
  data() {
    return {
      username: '',
      password: '',
      submitted: false,
    };
  },
  validations() {
    return {
      username: {
        required,
      },
      password: {
        required,
      },
    };
  },
  methods: {
    ...mapActions(['LogIn']),
    async handleSubmit(isFormValid) {
      if (!isFormValid) return;
      this.submitted = true;

      try {
        await this.LogIn(this.$data);
        await this.$router.push({ name: 'dashboard' });
      } catch (error) {
        const { response } = error;

        if (response?.status !== 200) {
          Object.values(response.data).forEach((errors) => {
            const iter = Array.isArray(errors) ? errors : [errors];

            iter.forEach((message) => {
              this.$toast.add({
                severity: 'error',
                summary: this.$t('status.error.title'),
                detail: message,
                life: 5000,
              });
            });
          });
        }
      }

      this.submitted = false;
    },
  },
};
</script>
