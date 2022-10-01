<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { useToast } from 'primevue/usetoast';
import { useUserStore } from '@/stores';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const router = useRouter();
const toast = useToast();
const { t } = useI18n();

const emit = defineEmits(['menu-toggle']);

function onMenuToggle(event: PointerEvent) {
  emit('menu-toggle', event);
}

async function handleSubmit() {
  await userStore.LogOut();
  toast.add({
    severity: 'success',
    summary: t('status.disconnection.title'),
    detail: t('status.disconnection.message'),
    life: 5000,
  });

  await router.push({ name: 'login' });
}
</script>

<template>
  <form class="layout-topbar">
    <router-link to="/" class="layout-topbar-logo">
      <img alt="SAURON logo" src="@/layout/images/logo.svg" />
    </router-link>
    <button
      type="button"
      class="p-link layout-menu-button layout-topbar-button"
      @click="onMenuToggle">
      <i class="pi pi-bars" />
    </button>

    <button
      type="button"
      class="p-link layout-topbar-menu-button layout-topbar-button"
      v-styleclass="{
        selector: '@next',
        enterClass: 'hidden',
        enterActiveClass: 'scalein',
        leaveToClass: 'hidden',
        leaveActiveClass: 'fadeout',
        hideOnOutsideClick: true,
      }">
      <i class="pi pi-ellipsis-v" />
    </button>
    <ul class="layout-topbar-menu hidden lg:flex origin-top lg:align-items-center">
      <li>
        <router-link :to="{ name: 'profile' }" v-slot="{ isActive, navigate }">
          <button
            type="button"
            :class="{ 'text-primary': isActive }"
            @click="navigate"
            class="p-link layout-topbar-button">
            <i class="pi pi-user" />
            <span>{{ $t('misc.profile') }}</span>
          </button>
        </router-link>
      </li>
      <li>
        <button
          type="button"
          @click="handleSubmit"
          class="p-link layout-topbar-button p-button-outlined">
          <i class="pi pi-sign-out" />
          <span>{{ $t('login.sign_out') }}</span>
        </button>
      </li>
    </ul>
  </form>
</template>
