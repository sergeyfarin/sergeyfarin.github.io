export default defineNuxtConfig({
  compatibilityDate: '2026-07-07',
  modules: [
    '@nuxt/eslint',
    '@nuxtjs/tailwindcss'
  ],
  app: {
    head: {
      title: 'nuxt-sergey',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'My incredible Nuxt.js project' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  }
})
