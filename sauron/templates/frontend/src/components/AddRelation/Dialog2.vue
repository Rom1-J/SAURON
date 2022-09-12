<template>
  <div class="absolute bottom-0 right-0 mb-8">
    <Button icon="pi pi-plus" class="p-button-rounded p-button-info m-5"
            @click="addDialogOpened = true"/>
  </div>

  <Dialog :header="$t('misc.add_relation')" v-model:visible="addDialogOpened"
          class="h-full w-full m-5"
          :modal="true" content-class="flex-1">

    <form @submit.prevent="handleSubmit()"
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
          <label for="firstname">
            {{ $t('fields.firstname') }}
          </label>

          <InputText v-model="form.firstName" id="firstname" type="text"/>
        </div>
        <div class="field col-12 md:col-6">
          <label for="lastname">
            {{ $t('fields.lastname') }}
          </label>
          <InputText v-model="form.lastName" id="lastname" type="text"/>
        </div>

        <div class="field col-12 mt-3">
          <label for="note">
            {{ $t('fields.note') }}
          </label>

          <Textarea :autoResize="true" rows="3" cols="30" v-model="form.note"/>
        </div>

        <div class="field col-12 mt-3">
          <label for="nicknames">
            {{ $t('fields.nicknames') }}
          </label>

          <Chips v-model="form.nicknames"/>
        </div>
      </template>

      <template v-if="currentTab === 'tags'">
        <div class="field col-12 md:col-12 mt-3">
          <label for="tags">
            {{ $t('fields.tags') }}
          </label>

          <div class="p-fluid formgrid grid">
            <div class="field col-10">
              <AutoComplete :dropdown="true" field="name" :multiple="true" v-model="form.tags"
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
        <template v-for="(link, i) in form.links" :key="`link-${i}`">
          <div class="field col-12 md:col-12 mt-3">
            <label :for="`link-${i}`">
              {{ $t('fields.link') }}
            </label>

            <div class="p-fluid formgrid grid">
              <div class="field col-10">
                <InputText type="text" v-model="link.link"/>
              </div>

              <div class="field col-2 align-self-center">
                <Button icon="pi pi-times" @click="removeLinkField(i)"
                        class="p-button w-full p-button-danger"/>
              </div>

              <div class="field col-12">
                <label for="note">
                  {{ $t('fields.note') }}
                </label>

                <Textarea :autoResize="true" rows="3" cols="30" v-model="link.note"/>
              </div>
            </div>
          </div>

          <Divider/>
        </template>

        <div class="field col-12 md:col-12 mt-3">
          <Button icon="pi pi-plus" @click="addLinkField" class="p-button p-button-sm"/>
        </div>
      </template>

      <template v-if="currentTab === 'files'">
        <div class="field col-12 md:col-12 mt-3">
          <label for="files">
            {{ $t('fields.files') }}
          </label>

          <FileUpload custom-upload @uploader="uploadFiles" :multiple="true"
                      :show-upload-button="false" ref="fileUpload" auto
                      :maxFileSize="1000000"/>
        </div>
      </template>

    </form>
    <template #footer>
      <Button :label="$t('fields.prev')" @click="prevTab()" icon="pi pi-chevron-left"
              class="p-button-outlined" v-if="availableTabs.indexOf(currentTab) > 0"/>

      <Button :label="$t('fields.save')" @click="handleSubmit()" icon="pi pi-check"
              class="p-button-success" :disabled="submitted"
              v-if="availableTabs.indexOf(currentTab) === availableTabs.length - 1"/>
      <Button :label="$t('fields.next')" @click="nextTab()" icon="pi pi-chevron-right"
              class="p-button-outlined" iconPos="right" v-else/>
    </template>
  </Dialog>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      addDialogOpened: true,
      form: {
        firstName: '',
        lastName: '',
        tags: [],
        links: [],
        note: '',
        nicknames: '',
      },
      tagsSuggested: [],
      tagsOptions: [],
      submitted: false,
      currentTab: 'files',
      availableTabs: ['personal', 'tags', 'links', 'files'],
    };
  },
  computed: {
    ...mapGetters(['StateTags']),
  },
  methods: {
    ...mapActions(['GetTags', 'CreateRelation']),
    searchTag(event) {
      if (!event.query.trim().length) this.tagsSuggested = [...this.tagsOptions];
      else {
        this.tagsSuggested = this.tagsOptions.filter(
          (tag) => tag.name.toLowerCase().includes(event.query.toLowerCase()),
        );
      }
    },
    removeLinkField(i) {
      this.form.links.splice(i, 1);
    },
    addLinkField() {
      this.form.links.push({});
    },
    prevTab() {
      const pos = this.availableTabs.indexOf(this.currentTab);

      if (pos > 0) {
        this.currentTab = this.availableTabs[pos - 1];
      }
    },
    nextTab() {
      const pos = this.availableTabs.indexOf(this.currentTab);

      if (pos < this.availableTabs.length) {
        this.currentTab = this.availableTabs[pos + 1];
      }
    },
    uploadFiles(event) {
      console.log(event);
      console.log(this.$refs.fileUpload);
    },
    async handleSubmit() {
      console.log(this.$refs.fileUpload);
      // if (this.form.firstName.trim() === '' || this.form.lastName.trim() === '') {
      //   this.$toast.add({
      //     severity: 'error',
      //     summary: this.$t('status.error.title'),
      //     detail: this.$t('status.error.invalid_personals'),
      //     life: 3000,
      //   });
      //   return;
      // }
      // this.submitted = true;
      //
      // try {
      //   this.CreateRelation(this.form);
      // } catch (error) {
      //   const { response } = error;
      //
      //   if (response?.status !== 200) {
      //     if (response.data) {
      //       Object.values(response.data).forEach((errors) => {
      //         const iter = Array.isArray(errors) ? errors : [errors];
      //
      //         iter.forEach((message) => {
      //           this.$toast.add({
      //             severity: 'error',
      //             summary: this.$t('status.error.title'),
      //             detail: message,
      //             life: 5000,
      //           });
      //         });
      //       });
      //     } else {
      //       this.$toast.add({
      //         severity: 'error',
      //         summary: this.$t('status.error.title'),
      //         detail: this.$t('status.error.unknown'),
      //         life: 5000,
      //       });
      //     }
      //   }
      // }
      //
      // this.submitted = false;
    },
  },
  async created() {
    if (this.StateTags.length === 0) await this.GetTags();
    this.tagsOptions = this.StateTags;
  },
};
</script>
