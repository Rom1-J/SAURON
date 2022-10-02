<script lang="ts" setup>
import { toRefs } from 'vue';
import { hexToRGB, hexToHSL } from '@/utils';
import { useUserStore } from '@/stores';

const userStore = useUserStore();

const props = defineProps<{
  name: string
  note?: string
  color: string
}>();

const { name, color, note } = toRefs(props);

function getColorVariables() {
  const rgb = hexToRGB(color.value || '#000000');
  const hsl = hexToHSL(color.value || '#000000');

  return {
    '--lightness-threshold': userStore.user?.theme === 'DK' ? 0.9 : 0.5,
    '--background-alpha': userStore.user?.theme === 'DK' ? 0.45 : 0.15,
    '--label-r': rgb.r,
    '--label-g': rgb.g,
    '--label-b': rgb.b,
    '--label-h': hsl.h,
    '--label-s': hsl.s,
    '--label-l': hsl.l,
  };
}
</script>

<template>
  <span
    class="p-tag p-component p-tag-rounded"
    :style="getColorVariables()">
    <span v-tooltip.top="note" class="p-tag-value">{{ name }}</span>
  </span>
</template>

<style lang="scss" scoped>
.p-tag {
  --border-alpha: 0.3;

  --perceived-lightness: calc( ((var(--label-r) * 0.2126) + (var(--label-g) * 0.7152) + (var(--label-b) * 0.0722)) / 255 );
  --lightness-switch: max(0, min(calc((var(--perceived-lightness) - var(--lightness-threshold)) * -1000), 1));

  --lighten-by: calc(((var(--lightness-threshold) - var(--perceived-lightness)) * 100) * var(--lightness-switch));

  color: hsl(var(--label-h), calc(var(--label-s) * 1%), calc((var(--label-l) + var(--lighten-by)) * 1%));
  background: rgba(var(--label-r), var(--label-g), var(--label-b), var(--background-alpha));
  border: 1px solid hsla(var(--label-h), calc(var(--label-s) * 1%), calc((var(--label-l) + var(--lighten-by)) * 1%), var(--border-alpha));
}
</style>
