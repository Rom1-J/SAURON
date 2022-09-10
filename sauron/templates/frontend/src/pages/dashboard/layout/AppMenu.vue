<template>
  <div class="layout-menu-container">
    <AppSubmenu :items="model" class="layout-menu" :root="true"
                @menuitem-click="onMenuItemClick" @keydown="onKeyDown"/>
  </div>
</template>

<script>
import AppSubmenu from './AppSubmenu.vue';

export default {
  props: {
    model: Array,
  },
  methods: {
    onMenuItemClick(e) {
      this.$emit('menuitem-click', e);
    },
    onKeyDown(e) {
      const nodeElement = e.target;
      if (e.code === 'Enter' || e.code === 'Space') {
        nodeElement.click();
        e.preventDefault();
      }
    },
  },
  components: {
    AppSubmenu,
  },
};
</script>
