import { defineConfig } from 'astro/config'
import react from '@astrojs/react'
import tailwind from '@astrojs/tailwind'

import sanity from '@sanity/astro'

// https://astro.build/config
export default defineConfig({
  integrations: [
    react(),
    tailwind(),
    sanity({
      projectId: '128fvw6m',
      dataset: 'production',
      useCdn: true,
      apiVersion: 'v2022-03-07'
    })
  ],
  server: {
    proxy: {
      '/api': {
        target: '',
        changeOrigin: true
      }
    }
  }
})
