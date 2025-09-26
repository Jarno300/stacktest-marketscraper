<template>
  <div class="max-w-6xl mx-auto p-4 space-y-4">
    <FilterBar @apply="fetchWith" />
    <div class="flex justify-between items-center">
      <h2 class="text-lg font-semibold">Results</h2>
      <span class="text-sm text-gray-600">Total: {{ total }}</span>
    </div>
    <div class="grid md:grid-cols-3 gap-4">
      <ListingCard v-for="it in items" :key="it.id" :item="it" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import FilterBar from "../components/FilterBar.vue";
import ListingCard from "../components/ListingCard.vue";
import { useApi } from "../composables/useApi";

const { fetchListings } = useApi();
const items = ref<any[]>([]);
const total = ref(0);

onMounted(() => fetchWith({}));

async function fetchWith(params: Record<string, any>) {
  const res = await fetchListings();
  items.value = res.items;
  total.value = res.total;
}
</script>
