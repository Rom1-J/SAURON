<script lang="ts" setup>
function getRelationsCount(): number {
  return 42;
}
</script>
<template>
  <div class="grid">
    <div class="col-12 lg:col-6">
      <div class="card mb-0">
        <div class="flex justify-content-between mb-3">
          <div>
            <span
              class="block text-500 font-medium mb-3">{{ $t('misc.relations') }}</span>
            <span class="text-900 font-medium text-8xl">
              {{ getRelationsCount() }}
            </span>
          </div>
          <div
            class="flex align-items-center justify-content-center bg-blue-100 border-round"
            style="width:4.5rem;height:4.5rem">
            <i class="pi pi-users text-5xl text-blue-500" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
