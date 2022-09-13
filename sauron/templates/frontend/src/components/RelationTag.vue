<script lang="ts" setup>

import { toRefs } from 'vue';

const props = defineProps<{
  name: string,
  color?: string,
  note?: string,
}>();

const { name, color, note } = toRefs(props);
</script>

<template>
  <template v-if="name">
    <span :style="{ backgroundColor: `#${color}` }" class="p-tag p-component p-tag-rounded">
      <span
        :style="{ color: `#${color}`, filter: 'invert(1)' }"
        v-tooltip.top="note"
        class="p-tag-value">
        {{ name }}
      </span>
    </span>
  </template>

  <template v-else>
    <span class="p-tag p-component p-tag-rounded">
      <span v-tooltip.top="note" class="p-tag-value">{{ name }}</span>
    </span>
  </template>
</template>
