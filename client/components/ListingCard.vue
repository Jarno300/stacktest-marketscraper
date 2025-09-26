<template>
  <div class="border rounded-xl overflow-hidden shadow">
    <img
      v-if="item.images?.length"
      :src="item.images[0]"
      alt=""
      class="w-full h-48 object-cover"
    />
    <div class="p-3 space-y-2">
      <div class="flex justify-between items-start gap-3">
        <h3 class="font-semibold line-clamp-2">{{ item.title }}</h3>
        <span class="text-sm bg-gray-100 px-2 py-1 rounded">{{
          item.platform
        }}</span>
      </div>
      <p class="text-sm text-gray-600 line-clamp-2">{{ item.description }}</p>
      <div class="flex items-center justify-between text-sm">
        <div>
          <span class="font-semibold"
            >€{{ (item.price_cents / 100).toFixed(2) }}</span
          >
          <span
            v-if="item.delivery_cost_cents != null"
            class="ml-2 text-gray-500"
            >+ ship €{{ (item.delivery_cost_cents / 100).toFixed(2) }}</span
          >
        </div>
        <div v-if="item.distance_km != null" class="text-gray-600">
          {{ item.distance_km }} km
        </div>
      </div>
      <div class="flex justify-between items-center text-xs text-gray-500">
        <span v-if="item.city">{{ item.postal_code }} {{ item.city }}</span>
        <a :href="item.url" target="_blank" class="underline">Open</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{ item: any }>();
</script>
