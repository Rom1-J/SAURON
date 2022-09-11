<template>
  <div class="absolute bottom-0 right-0 mb-8">
    <Button icon="pi pi-plus" class="p-button-rounded p-button-info m-4"
            @click="addDialogOpened = true"/>
  </div>

  <Dialog :header="$t('misc.add_relation')" v-model:visible="addDialogOpened"
          :breakpoints="{'960px': '75vw'}" :style="{width: '45vw', minHeight: '70vh'}"
          :modal="true" content-class="flex-1">

    <form @submit.prevent="handleSubmit(!v$.$invalid)"
          class="p-fluid formgrid grid">

      <div class="field col-12">
        <div class="p-tabmenu p-component">
          <ul ref="nav" class="p-tabmenu-nav p-reset" role="tablist">
            <li role="tab" class="p-tabmenuitem"
                :class="{'p-highlight': currentTab === 'personal'}">
              <a class="p-menuitem-link" role="presentation" @click="currentTab = 'personal'">
                <span class="p-menuitem-text">Personal</span>
              </a>
            </li>

            <li role="tab" class="p-tabmenuitem"
                :class="{'p-highlight': currentTab === 'tags'}">
              <a class="p-menuitem-link" role="presentation" @click="currentTab = 'tags'">
                <span class="p-menuitem-text">Tags</span>
              </a>
            </li>

            <li role="tab" class="p-tabmenuitem"
                :class="{'p-highlight': currentTab === 'links'}">
              <a class="p-menuitem-link" role="presentation" @click="currentTab = 'links'">
                <span class="p-menuitem-text">Links</span>
              </a>
            </li>

            <li role="tab" class="p-tabmenuitem"
                :class="{'p-highlight': currentTab === 'files'}">
              <a class="p-menuitem-link" role="presentation" @click="currentTab = 'files'">
                <span class="p-menuitem-text">Files</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <template v-if="currentTab === 'personal'">
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

        <div class="field col-12 mt-3">
          <label for="note">
            {{ $t('fields.note') }}
          </label>

          <Textarea :autoResize="true" rows="3" cols="30" v-model="note"/>
        </div>

        <div class="field col-12 mt-3">
          <label for="nicknames">
            {{ $t('fields.nicknames') }}
          </label>

          <Chips v-model="nicknames"/>
        </div>
      </template>

      <template v-if="currentTab === 'tags'">
        <div class="field col-12 md:col-12 mt-3">
          <label for="tags">
            {{ $t('fields.tags') }}
          </label>

          <div class="p-fluid formgrid grid">
            <div class="field col-10">
              <AutoComplete :dropdown="true" field="name" :multiple="true" v-model="tags"
                            :suggestions="tagsSuggested" @complete="searchTag($event)"/>
            </div>

            <div class="field col-2 align-self-center">
              <Button icon="pi pi-plus" class="p-button w-full"
                      @click="addDialogOpened = true"/>
            </div>
          </div>
        </div>
      </template>

      <template v-if="currentTab === 'links'">
        <div class="field col-12 md:col-12 mt-3">
          <label for="links">
            {{ $t('fields.links') }}
          </label>

          <div class="p-fluid formgrid grid">
            <div class="field col-10">
              <InputText type="text"/>
            </div>

            <div class="field col-2 align-self-center">
              <Button icon="pi pi-times" class="p-button w-full p-button-danger"/>
            </div>
          </div>

          <div class="p-fluid formgrid grid">
            <div class="field col-10">
              <InputText type="text"/>
            </div>

            <div class="field col-2 align-self-center">
              <Button icon="pi pi-times" class="p-button w-full p-button-danger"/>
            </div>
          </div>

          <div class="grid">
            <div class="col-2">
              <Button icon="pi pi-plus" class="p-button p-button-sm"/>
            </div>
          </div>
        </div>
      </template>

      <template v-if="currentTab === 'files'">
        <div class="field col-12 md:col-12 mt-3">
          <label for="files">
            {{ $t('fields.files') }}
          </label>

          <FileUpload :multiple="true" :maxFileSize="1000000"/>
        </div>
      </template>

    </form>
    <template #footer>
      <Button :label="$t('fields.add')" @click="addDialogOpened = false" icon="pi pi-check"
              class="p-button-outlined"/>
    </template>
  </Dialog>
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
      addDialogOpened: true,
      firstName: '',
      lastName: '',
      tags: [],
      tagsSuggested: [],
      tagsOptions: [],
      note: '',
      nicknames: '',
      submitted: false,
      currentTab: 'personal',
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
    ...mapGetters(['StateTags']),
  },
  methods: {
    ...mapActions(['GetTags']),
    async handleSubmit(isFormValid) {
      if (!isFormValid) return;
      this.submitted = true;

      this.submitted = false;
    },
    searchTag(event) {
      if (!event.query.trim().length) this.tagsSuggested = [...this.tagsOptions];
      else {
        this.tagsSuggested = this.tagsOptions.filter(
          (tag) => tag.name.toLowerCase().includes(event.query.toLowerCase()),
        );
      }
    },
  },
  async created() {
    if (this.StateTags.length === 0) await this.GetTags();
    this.tagsOptions = this.StateTags;
  },
};
</script>
