import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: false,
    // Fonts stay as same-origin files so the strict font-src policy in netlify.toml permits them.
    assetsInlineLimit: 0,
  },
  server: {
    // `npm run serve` runs the built app and the functions on 127.0.0.1:8888; `npm run dev` proxies the API to it.
    proxy: { "/api": { target: "http://127.0.0.1:8888", changeOrigin: false } },
  },
});
