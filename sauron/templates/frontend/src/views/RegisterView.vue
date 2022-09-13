<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { computed, reactive, ref } from 'vue';
import { useVuelidate } from '@vuelidate/core';
import { useToast } from 'primevue/usetoast';
import { required, sameAs, email } from '@vuelidate/validators';

import { useUserStore } from '@/stores';
import { useI18n } from 'vue-i18n';
import axios, { AxiosError } from 'axios';
import { ServerError } from '@/types/server';

const userStore = useUserStore();
const router = useRouter();
const toast = useToast();

const { t } = useI18n();

const submitted = ref(false);

const state = reactive({
  username: '',
  email: '',
  password1: '',
  password2: '',
});

const passwordRef = computed(() => state.password1);

const rules = {
  username: {
    required,
  },
  email: {
    required,
    email,
  },
  password1: {
    required,
  },
  password2: {
    required,
    sameAsPassword: sameAs(passwordRef),
  },
};

const v$ = useVuelidate(rules, state);

async function handleSubmit(isFormValid: boolean) {
  if (!isFormValid) return;
  submitted.value = true;

  try {
    await userStore.Register(state);
    toast.add({
      severity: 'info',
      summary: t('status.confirmation'),
      detail: t('register.success_creation'),
      life: 5000,
    });
    await router.push({ name: 'login' });
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const serverError = error as AxiosError<ServerError>;

      if (serverError && serverError.response) {
        Object.values(serverError.response.data).forEach((errors) => {
          const iter = Array.isArray(errors) ? errors : [errors];

          iter.forEach((message) => {
            toast.add({
              severity: 'error',
              summary: t('status.error.title'),
              detail: message,
              life: 5000,
            });
          });
        });
      } else {
        toast.add({
          severity: 'error',
          summary: t('status.error.title'),
          detail: t('status.error.unknown'),
          life: 5000,
        });
      }
    }
  }

  submitted.value = false;
}
</script>

<template>
  <div
    class="surface-0 flex align-items-center justify-content-center
       min-h-screen min-w-screen overflow-hidden">
    <div class="grid justify-content-center p-2 lg:p-0" style="min-width:80%">
      <div class="col-12 mt-5 xl:mt-0 text-center">
        <router-link
          :to="{ name: 'landing' }"
          class="hover:underline">
          <img
            src="@/layout/images/logo.svg"
            alt="SAURON logo"
            class="mb-5"
            height="64">
        </router-link>
      </div>
      <div
        class="col-12 xl:col-6"
        style="border-radius:56px; padding:0.3rem;
           background: linear-gradient(180deg, var(--primary-color), rgba(33, 150, 243, 0) 30%);">
        <div
          class="h-full w-full m-0 py-7 px-4"
          style="border-radius:53px;
             background: linear-gradient(180deg, var(--surface-50) 38.9%, var(--surface-0));">
          <div class="text-center mb-5">
            <div class="text-900 text-3xl font-medium">
              {{ $t('register.create_account') }}
            </div>
            <span class="text-600 font-medium">
              {{ $t('register.already_registered') }}
              <router-link
                :to="{ name: 'login' }"
                class="hover:underline">
                {{ $t('login.sign_in') }}
              </router-link>
            </span>
          </div>

          <form
            @submit.prevent="handleSubmit(!v$.$invalid)"
            class="w-full md:w-10 mx-auto">
            <div class="field">
              <label
                for="username"
                :class="{ 'p-error': v$.username.$invalid && v$.username.$model }"
                class="block text-900 text-xl font-medium mb-2">
                {{ $t('fields.username') }}*
              </label>

              <InputText
                id="username"
                v-model="v$.username.$model"
                :class="{ 'p-invalid': v$.username.$invalid && v$.username.$model }"
                class="w-full"
                type="text"
                :placeholder="$t('fields.username')"
                style="padding:1rem;" />
              <ul
                class="p-0 mt-0 list-none"
                v-if="(v$.username.$invalid && v$.username.$model)
                  || v$.username.$pending.$response">
                <li v-if="v$.username.required.$invalid" class="p-error">
                  {{ v$.username.required.$message }}
                </li>
              </ul>
            </div>

            <div class="field">
              <label
                for="email"
                :class="{ 'p-error': v$.email.$invalid && v$.email.$model }"
                class="block text-900 text-xl font-medium mb-2">
                {{ $t('fields.email') }}*
              </label>
              <InputText
                id="email"
                v-model="v$.email.$model"
                :class="{ 'p-invalid': v$.email.$invalid && v$.email.$model }"
                class="w-full"
                type="email"
                :placeholder="$t('fields.email')"
                style="padding:1rem;" />
              <ul
                class="p-0 mt-0 list-none"
                v-if="(v$.email.$invalid && v$.email.$model)
                  || v$.email.$pending.$response">
                <li v-if="v$.email.required.$invalid" class="p-error">
                  {{ v$.email.required.$message }}
                </li>
                <li v-if="v$.email.email.$invalid" class="p-error">
                  {{ v$.email.email.$message }}
                </li>
              </ul>
            </div>

            <div class="field">
              <label
                for="password1"
                :class="{ 'p-error': v$.password1.$invalid && v$.password1.$model }"
                class="block text-900 font-medium text-xl mb-2">
                {{ $t('fields.password') }}*
              </label>
              <Password
                id="password1"
                v-model="v$.password1.$model"
                :placeholder="$t('fields.password')"
                :class="{ 'p-invalid': v$.password1.$invalid && v$.password1.$model }"
                toggleMask
                class="w-full"
                inputClass="w-full"
                inputStyle="padding:1rem" />
              <ul
                class="p-0 mt-0 list-none"
                v-if="(v$.password1.$invalid && v$.password1.$model)
                  || v$.password1.$pending.$response">
                <li v-if="v$.password1.required.$invalid" class="p-error">
                  {{ v$.password1.required.$message }}
                </li>
              </ul>
            </div>

            <div class="field">
              <label
                for="password2"
                :class="{ 'p-error': v$.password2.$invalid && v$.password2.$model }"
                class="block text-900 font-medium text-xl mb-2">
                {{ $t('fields.confirm_password') }}*
              </label>
              <Password
                id="password2"
                v-model="v$.password2.$model"
                :placeholder="$t('fields.confirm_password')"
                :class="{ 'p-invalid': v$.password2.$invalid && v$.password2.$model }"
                :toggleMask="true"
                class="w-full"
                inputClass="w-full"
                inputStyle="padding:1rem" />
              <ul
                class="p-0 mt-0 list-none"
                v-if="(v$.password2.$invalid && v$.password2.$model)
                  || v$.password2.$pending.$response">
                <li v-if="v$.password2.required.$invalid" class="p-error">
                  {{ v$.password2.required.$message }}
                </li>
                <li
                  v-if="v$.password2.sameAsPassword.$invalid"
                  class="p-error">
                  {{ v$.password2.sameAsPassword.$message }}
                </li>
              </ul>
            </div>

            <Button
              type="submit"
              :label="$t('register.sign_up')"
              class="w-full p-3 text-xl"
              :disabled="v$.$invalid || submitted" />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
