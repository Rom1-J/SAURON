<script lang="ts" setup>
import AppSubmenu from './AppSubmenu.vue';

const props = defineProps(['model']);
const emit = defineEmits(['menuitem-click']);

function onMenuItemClick(e: Event) {
  emit('menuitem-click', e);
}

function onKeyDown(e: KeyboardEvent) {
  const nodeElement = e.target as HTMLInputElement;
  if (!nodeElement) return;

  if (e.code === 'Enter' || e.code === 'Space') {
    nodeElement.click();
    e.preventDefault();
  }
}
</script>

<template>
  <div class="layout-menu-container">
    <AppSubmenu
      :items="props.model"
      class="layout-menu"
      :root="true"
      @menuitem-click="onMenuItemClick"
      @keydown="onKeyDown" />
  </div>
</template>
