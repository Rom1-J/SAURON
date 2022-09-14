<script lang="ts" setup>
import { useUserStore } from '@/stores';

const userStore = useUserStore();
</script>
<template>
  <component :is="'style'" v-if="userStore.isAuthenticated && userStore.user?.theme === 'DK'">
    @import '/themes/lara-dark-purple/theme.css';
  </component>

  <component :is="'style'" v-else>
    @import '/themes/lara-light-purple/theme.css';
  </component>

  <router-view />
  <Toast />
</template>
