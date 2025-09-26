export default defineNuxtConfig({
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      // Default for local dev; override via .env -> NUXT_PUBLIC_API_BASE
      apiBase: "http://localhost:8000",
    },
  },
});
