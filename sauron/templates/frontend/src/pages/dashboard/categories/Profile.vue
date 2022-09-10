<template>
  <div class="grid">
    <div class="col-12">
      <div class="card">
        <h5>{{ StateUser.username }}</h5>
        <form @submit.prevent="handleSubmit(!v$.$invalid)"
              class="p-fluid formgrid grid">
          <div class="field col-12 md:col-4">
            <label for="username">
              {{ $t('fields.username') }}
            </label>
            <InputText v-model="username" id="username" disabled type="text"/>
          </div>
          <div class="field col-12 md:col-4">
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
          <div class="field col-12 md:col-4">
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
          <div class="field col-12">
            <label for="email">
              {{ $t('fields.email') }}
            </label>
            <InputText v-model="email" id="email" disabled type="email"/>
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
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      friendCode: '',
      publicKey: '',
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
        this.$router.push({ name: 'login' });
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
    this.firstName = this.StateUser.first_name;
    this.lastName = this.StateUser.last_name;
    this.email = this.StateUser.email;
  },
};
</script>
