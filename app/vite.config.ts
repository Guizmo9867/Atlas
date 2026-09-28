import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Le corpus (dossier data/ à la racine du dépôt) reste indépendant du code :
// on autorise Vite à le lire depuis le dossier parent.
export default defineConfig({
  plugins: [react()],
  server: { fs: { allow: ['..'] }, open: true },
  worker: { format: 'es' },
  build: { chunkSizeWarningLimit: 2000 }, // MapLibre pèse ~1 Mo, c'est normal
})
