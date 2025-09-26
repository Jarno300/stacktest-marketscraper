import { useRuntimeConfig } from "nuxt/app";

export function useApi() {
  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase;

  async function fetchListings() {
    const response = await fetch(`${apiBase}/api/listings`);
    if (!response.ok) {
      throw new Error("Failed to fetch listings");
    }
    return response.json();
  }

  return {
    fetchListings,
  };
}
