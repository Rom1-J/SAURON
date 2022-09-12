<template>
  <template v-if="getColor()">
    <span :style="{backgroundColor: `#${getColor()}`}" class="p-tag p-component p-tag-rounded">
      <span :style="{color: `#${getColor()}`, filter: 'invert(1)'}"
             v-tooltip.top="getNote()" class="p-tag-value">
        {{ getName() }}
      </span>
    </span>
  </template>

  <template v-else>
    <span class="p-tag p-component p-tag-rounded">
      <span v-tooltip.top="getNote()" class="p-tag-value">{{ getName() }}</span>
    </span>
  </template>
</template>

<script>
export default {
  props: {
    tag: {
      type: Object,
      required: false,
      default: () => {},
    },
    name: {
      type: String,
      required: false,
      default: '',
    },
    color: {
      type: String,
      required: false,
      default: '',
    },
    note: {
      type: String,
      required: false,
      default: '',
    },
  },
  methods: {
    getName() {
      if (this.tag && this.tag.name !== undefined) return this.tag.name;
      return this.name;
    },
    getColor() {
      if (this.tag && this.tag.color !== undefined) return this.tag.color;
      return this.color;
    },
    getNote() {
      if (this.tag && this.tag.note !== undefined) return this.tag.note;
      return this.note;
    },
  },
};
</script>
