<template>
  <form class="layout-topbar">
    <router-link to="/" class="layout-topbar-logo">
      <img alt="SAURON logo" src="@/layout/images/logo.svg"/>
    </router-link>
    <button class="p-link layout-menu-button layout-topbar-button"
            @click="onMenuToggle">
      <i class="pi pi-bars"></i>
    </button>

    <button class="p-link layout-topbar-menu-button layout-topbar-button"
            v-styleclass="{ selector: '@next', enterClass: 'hidden', enterActiveClass: 'scalein',
            leaveToClass: 'hidden', leaveActiveClass: 'fadeout', hideOnOutsideClick: true}">
      <i class="pi pi-ellipsis-v"></i>
    </button>
    <ul class="layout-topbar-menu hidden lg:flex origin-top lg:align-items-center">
      <li>
        <router-link :to="{name: 'profile'}" v-slot="{ isActive, navigate }">
          <button :class="{'text-primary': isActive}" @click="navigate"
                  class="p-link layout-topbar-button">
            <i class="pi pi-user"></i>
            <span>{{ $t('misc.profile') }}</span>
          </button>
        </router-link>
      </li>
      <li>
        <Button @click="handleSubmit" class="p-link layout-topbar-button">
          <i class="pi pi-sign-out"></i>
          <span>{{ $t('login.sign_out') }}</span>
        </Button>
      </li>
    </ul>
  </form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  methods: {
    ...mapActions(['LogOut']),
    onMenuToggle(event) {
      this.$emit('menu-toggle', event);
    },
    async handleSubmit() {
      await this.LogOut();
      this.$toast.add({
        severity: 'success',
        summary: this.$t('status.disconnection.title'),
        detail: this.$t('status.disconnection.message'),
        life: 5000,
      });

      await this.$router.push({ name: 'login' });
    },
  },
};
</script>
