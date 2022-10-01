<script lang="ts" setup>
// eslint-disable-next-line import/no-unresolved
import AddRelationDialog from '@/components/AddRelation.vue';

import { reactive } from 'vue';
import { useI18n } from 'vue-i18n';
import { usePrimeVue } from 'primevue/config';
import { DashboardItemType, DashboardMenuItemEvent } from '@/types/dashboard';
import AppTopBar from './layout/AppTopbar.vue';
import AppMenu from './layout/AppMenu.vue';
import AppFooter from './layout/AppFooter.vue';

const { t } = useI18n();
const primevue = usePrimeVue();

function isDesktop(): boolean {
  return window.innerWidth >= 992;
}

const state = reactive({
  layoutMode: 'static',
  menuClick: false,
  staticMenuInactive: false,
  overlayMenuActive: false,
  mobileMenuActive: false,
  menu: [
    {
      label: t('misc.home'),
      items: [{
        label: t('misc.dashboard'),
        icon: 'pi pi-fw pi-home',
        to: { name: 'dashboard' },
      }],
    },
    {
      label: t('status.exchange.title'),
      items: [
        {
          label: t('status.exchange.empty'),
        },
      ],
    },
  ] as DashboardItemType[],
});

function onWrapperClick() {
  if (!state.menuClick) {
    state.overlayMenuActive = false;
    state.mobileMenuActive = false;
  }

  state.menuClick = false;
}

function onMenuToggle(event: PointerEvent) {
  state.menuClick = true;

  if (isDesktop()) {
    if (state.layoutMode === 'overlay') {
      if (state.mobileMenuActive === true) {
        state.overlayMenuActive = true;
      }

      state.overlayMenuActive = !state.overlayMenuActive;
      state.mobileMenuActive = false;
    } else if (state.layoutMode === 'static') {
      state.staticMenuInactive = !state.staticMenuInactive;
    }
  } else {
    state.mobileMenuActive = !state.mobileMenuActive;
  }

  event.preventDefault();
}

function onSidebarClick() {
  state.menuClick = true;
}

function onMenuItemClick(event: DashboardMenuItemEvent) {
  if (event.item && !event.item.items) {
    state.overlayMenuActive = false;
    state.mobileMenuActive = false;
  }
}

function containerClass() {
  return [
    'layout-wrapper', {
      'layout-overlay': state.layoutMode === 'overlay',
      'layout-static': state.layoutMode === 'static',
      'layout-static-sidebar-inactive': state.staticMenuInactive && state.layoutMode === 'static',
      'layout-overlay-sidebar-active': state.overlayMenuActive && state.layoutMode === 'overlay',
      'layout-mobile-sidebar-active': state.mobileMenuActive,
      'p-input-filled': primevue.config.inputStyle === 'filled',
      'p-ripple-disabled': primevue.config.ripple === false,
    },
  ];
}
</script>

<template>
  <div :class="containerClass()" @click="onWrapperClick">
    <AppTopBar @menu-toggle="onMenuToggle" />
    <div class="layout-sidebar" @click="onSidebarClick">
      <AppMenu :model="state.menu" @menuitem-click="onMenuItemClick" />
    </div>

    <div class="layout-main-container">
      <div class="layout-main">
        <router-view :key="$route.fullPath" />
      </div>
      <AppFooter />
    </div>

    <transition name="layout-mask">
      <div
        class="layout-mask p-component-overlay"
        v-if="state.mobileMenuActive" />
    </transition>

    <AddRelationDialog />
  </div>
</template>

<style lang="scss">
@import './App.scss';
</style>
