<template>
  <Dialog :header="$t('misc.edit_tag')" v-model:visible="dialogOpened"
          :modal="true" content-class="flex-1">
    <template #header>
<span class="p-dialog-title">
{{ $t('misc.edit_tag') }}
</span>
      <RelationTag v-if="form.name" :name="form.name" :color="form.color" :note="form.note"/>
    </template>

    <form class="p-fluid formgrid grid">
      <div class="field col-10">
        <label for="name"
               :class="{'p-error':v$.form.name.$invalid && v$.form.name.$model}">
          {{ $t('fields.name') }}
        </label>

        <InputText v-model="v$.form.name.$model" id="name" type="text" class="p-inputtext-sm"
                   :class="{'p-invalid':v$.form.name.$invalid && v$.form.name.$model}"/>
      </div>

      <div class="field col-2">
        <label for="color">
          {{ $t('fields.color') }}
        </label>

        <ColorPicker v-model="form.color" id="color" default-color="000000"/>
      </div>

      <div class="field col-12">
        <label for="note">
          {{ $t('fields.note') }}
        </label>

        <Textarea :autoResize="true" id="note" rows="3" cols="30" v-model="form.note"/>
      </div>
    </form>

    <template #footer>
      <Button :label="$t('fields.save_edit')" icon="pi pi-check" @click="handleSubmit(!v$.$invalid)"
              class="p-button-success" iconPos="right" :disabled="v$.$invalid || submitted"/>
    </template>
  </Dialog>
</template>

<script>
import { required } from '@vuelidate/validators';
import { useVuelidate } from '@vuelidate/core';
import { mapActions } from 'vuex';

import axios from 'axios';

// eslint-disable-next-line import/no-unresolved
import RelationTag from '@/components/RelationTag.vue';

export default {
  setup() {
    return { v$: useVuelidate() };
  },
  props: {
    tagData: {
      type: Object,
      required: false,
      default: () => {
      },
    },
  },
  components: {
    RelationTag,
  },
  data() {
    return {
      dialogOpened: true,
      submitted: false,
      form: {
        name: '',
        color: '000000',
        note: '',
      },
    };
  },
  validations() {
    return {
      form: {
        name: {
          required,
        },
      },
    };
  },
  methods: {
    ...mapActions(['GetTags']),
    async handleSubmit(isFormValid) {
      if (!isFormValid) return;
      this.submitted = true;

      try {
        await axios.post('/api/tags/', this.form);
        this.$toast.add({
          severity: 'info',
          summary: this.$t('status.confirmation'),
          detail: this.$t('tag.success_creation'),
          life: 5000,
        });
        await this.GetTags();
      } catch (error) {
        const { response } = error;

        if (response?.status !== 200) {
          if (response.data) {
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
          } else {
            this.$toast.add({
              severity: 'error',
              summary: this.$t('status.error.title'),
              detail: this.$t('status.error.unknown'),
              life: 5000,
            });
          }
        }
      }

      this.submitted = false;
    },
  },
};
</script>
