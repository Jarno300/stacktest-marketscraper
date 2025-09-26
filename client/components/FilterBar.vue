<template>
  <div class="grid gap-3 md:grid-cols-6 p-3 bg-gray-50 rounded-xl shadow">
    <div class="md:col-span-2">
      <label class="block text-sm">Search</label>
      <input
        v-model="local.q"
        class="w-full border rounded p-2"
        placeholder="title/description"
      />
    </div>
    <div>
      <label class="block text-sm">Platform</label>
      <select v-model="local.platform" class="w-full border rounded p-2">
        <option value="">All</option>
        <option value="vinted">Vinted</option>
        <option value="2dehands">2dehands</option>
        <option value="facebook">Facebook</option>
      </select>
    </div>
    <div>
      <label class="block text-sm">Postal code (BE)</label>
      <input
        v-model="local.postal_code"
        class="w-full border rounded p-2"
        placeholder="e.g. 3000"
      />
    </div>
    <div>
      <label class="block text-sm">Max km</label>
      <input
        type="number"
        v-model.number="local.max_km"
        class="w-full border rounded p-2"
        placeholder="25"
      />
    </div>
    <div>
      <label class="block text-sm">Price (€)</label>
      <div class="flex gap-2">
        <input
          type="number"
          v-model.number="local.min_price_eur"
          class="w-full border rounded p-2"
          placeholder="min"
        />
        <input
          type="number"
          v-model.number="local.max_price_eur"
          class="w-full border rounded p-2"
          placeholder="max"
        />
      </div>
    </div>
    <div class="flex items-end">
      <button @click="apply" class="px-4 py-2 rounded-lg bg-black text-white">
        Apply
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from "vue";

const emit = defineEmits<{ (e: "apply", params: Record<string, any>): void }>();
const local = reactive({
  q: "",
  platform: "",
  postal_code: "",
  max_km: undefined as number | undefined,
  min_price_eur: undefined as number | undefined,
  max_price_eur: undefined as number | undefined,
});

function apply() {
  const params: Record<string, any> = {};
  if (local.q) params.q = local.q;
  if (local.platform) params.platform = local.platform;
  if (local.postal_code) params.postal_code = local.postal_code;
  if (typeof local.max_km === "number") params.max_km = local.max_km;
  if (typeof local.min_price_eur === "number")
    params.min_price = Math.round(local.min_price_eur * 100);
  if (typeof local.max_price_eur === "number")
    params.max_price = Math.round(local.max_price_eur * 100);
  emit("apply", params);
}
</script>
