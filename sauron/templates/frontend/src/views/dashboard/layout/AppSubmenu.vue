<script lang="ts" setup>
import { ref } from 'vue';
import { DashboardItemType } from '@/types/dashboard';

const props = defineProps({
  items: {
    default: () => {},
    type: Object,
  },
  root: {
    default: () => {},
    type: Object,
  },
});
const emit = defineEmits(['menuitem-click']);

const activeIndex = ref(null as number | null);

function onMenuItemClick(event: PointerEvent, item: DashboardItemType, index: number) {
  if (item.disabled) {
    event.preventDefault();
    return;
  }

  if (!item.to && !item.url) {
    event.preventDefault();
  }

  if (item.command) {
    item.command({ originalEvent: event, item });
  }

  activeIndex.value = index === activeIndex.value ? null : index;

  emit('menuitem-click', {
    originalEvent: event,
    item,
  });
}

function visible(item: DashboardItemType): boolean {
  return (typeof item.visible === 'function' ? item.visible() : item.visible !== false);
}
</script>

<template>
  <ul v-if="props.items">
    <template v-for="(item, i) of items">
      <li
        v-if="visible(item) && !item.separator"
        :key="item.label || i"
        :class="[{
          'layout-menuitem-category': root,
          'active-menuitem': activeIndex === i && !item.to && !item.disabled,
        }]"
        role="none">
        <template v-if="root">
          <div class="layout-menuitem-root-text" :aria-label="item.label">
            {{ item.label }}
          </div>
          <app-submenu
            :items="visible(item) && item.items"
            @menuitem-click="$emit('menuitem-click', $event)" />
        </template>
        <template v-else>
          <router-link
            v-if="item.to"
            :to="item.to"
            :class="[item.class, 'p-ripple', { 'p-disabled': item.disabled }]"
            :style="item.style"
            @click="onMenuItemClick($event, item, i)"
            :target="item.target"
            :aria-label="item.label"
            exact
            role="menuitem"
            v-ripple>
            <i :class="item.icon" />
            <span>{{ item.label }}</span>
            <i
              v-if="item.items"
              class="pi pi-fw pi-angle-down menuitem-toggle-icon" />
            <Badge v-if="item.badge" :value="item.badge" />
          </router-link>
          <a
            v-if="!item.to"
            :href="item.url || '#'"
            :style="item.style"
            :class="[item.class, 'p-ripple', { 'p-disabled': item.disabled }]"
            @click="onMenuItemClick($event, item, i)"
            :target="item.target"
            :aria-label="item.label"
            role="menuitem"
            v-ripple>
            <i :class="item.icon" />
            <span>{{ item.label }}</span>
            <i
              v-if="item.items"
              class="pi pi-fw pi-angle-down menuitem-toggle-icon" />
            <Badge v-if="item.badge" :value="item.badge" />
          </a>
          <transition name="layout-submenu-wrapper">
            <app-submenu
              v-show="activeIndex === i"
              :items="visible(item) && item.items"
              @menuitem-click="$emit('menuitem-click', $event)" />
          </transition>
        </template>
      </li>
      <li
        class="p-menu-separator"
        :style="item.style"
        v-if="visible(item) && item.separator"
        :key="`separator${i}`"
        role="separator" />
    </template>
  </ul>
</template>
