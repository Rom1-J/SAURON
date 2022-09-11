<template>
  <div class="grid">
    <div class="col-12">
      <div class="card">
        <div class="grid">
          <div class="col-6 mb-4">
            <span class="text-2xl mr-1">{{ StateUser.username }}</span>
            <i class="text-sm">({{ StateUser.email }})</i>
          </div>
          <div class="col-6 text-right">
            <img src="https://via.placeholder.com/32" alt="Avatar">
          </div>
        </div>
        <form @submit.prevent="handleSubmit(!v$.$invalid)"
              class="p-fluid formgrid grid">
          <div class="field col-12 md:col-6">
            <label for="firstname"
                   :class="{'p-error':v$.firstName.$invalid && submitted}">
              {{ $t('fields.firstname') }}
            </label>
            <InputText v-model="v$.firstName.$model" id="firstname"
                       :class="{'p-invalid':v$.firstName.$invalid && submitted}"
                       type="text"/>
            <small v-if="(v$.firstName.$invalid && submitted) || v$.firstName.$pending.$response"
                   class="p-error">
              {{ v$.firstName.alpha.$message }}
            </small>
          </div>
          <div class="field col-12 md:col-6">
            <label for="lastname"
                   :class="{'p-error':v$.lastName.$invalid && submitted}">
              {{ $t('fields.lastname') }}
            </label>
            <InputText v-model="v$.lastName.$model" id="lastname"
                       :class="{'p-invalid':v$.lastName.$invalid && submitted}"
                       type="text"/>
            <small v-if="(v$.lastName.$invalid && submitted) || v$.lastName.$pending.$response"
                   class="p-error">
              {{ v$.lastName.alpha.$message }}
            </small>
          </div>
          <div class="field col-12 md:col-4">
            <label for="language">
              {{ $t('fields.language') }}
            </label>
            <Dropdown v-model="language" :options="languageOptions"
                      optionLabel="name" id="language"/>
          </div>

          <div class="field col-12 md:col-4">
            <label for="theme">
              {{ $t('fields.theme.title') }}
            </label>
            <Dropdown v-model="theme" :options="themeOptions"
                      optionLabel="name" id="theme"/>
          </div>

          <div class="field col-12 md:col-4">
            <label for="avatar">
              {{ $t('fields.avatar') }}
            </label>
            <FileUpload mode="basic" v-model="avatar" class="w-full"
                        :choose-label="$t('fields.choose')"
                        name="avatar" accept="image/*" :maxFileSize="1000000"/>
          </div>

          <div class="field col-12 mt-5">
            <Button :label="$t('status.save')" :disabled="submitted || v$.$invalid" type="submit"/>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import { useVuelidate } from '@vuelidate/core';
import { alpha } from '@vuelidate/validators';

export default {
  setup() {
    return { v$: useVuelidate() };
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      language: '',
      languageOptions: [
        { name: 'Francais', code: 'FR' },
        { name: 'English', code: 'EN' },
      ],
      theme: '',
      themeOptions: [
        { name: this.$t('fields.theme.dark'), code: 'DK' },
        { name: this.$t('fields.theme.light'), code: 'LT' },
      ],
      avatar: '',
      submitted: false,
    };
  },
  validations() {
    return {
      firstName: {
        alpha,
      },
      lastName: {
        alpha,
      },
    };
  },
  computed: {
    ...mapGetters(['StateUser']),
  },
  methods: {
    ...mapActions(['UpdateUser']),
    async handleSubmit(isFormValid) {
      if (!isFormValid) return;
      this.submitted = true;

      try {
        await this.UpdateUser(this.$data);
        this.$toast.add({
          severity: 'success',
          summary: this.$t('status.saved.title'),
          detail: this.$t('status.saved.message'),
          life: 5000,
        });
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
  created() {
    this.username = this.StateUser.username;
    this.email = this.StateUser.email;
    this.firstName = this.StateUser.first_name;
    this.lastName = this.StateUser.last_name;
    this.language = this.StateUser.language;
    this.theme = this.StateUser.theme;
  },
};
</script>
