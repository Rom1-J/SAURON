<script lang="ts" setup>
import { useUserStore } from '@/stores';

const userStore = useUserStore();
</script>
<template>
  <component :is="'style'" v-if="userStore.isAuthenticated && userStore.user?.theme === 'DK'">
    @import '/themes/lara-dark-blue/theme.css';
  </component>

  <component :is="'style'" v-else>
    @import '/themes/lara-light-blue/theme.css';
  </component>

  <router-view />
  <Toast position="top-left" />
</template>
