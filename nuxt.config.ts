// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Enable Tailwind CSS
  modules: ['@nuxtjs/tailwindcss'],
  
  // Configure app settings
  app: {
    head: {
      title: 'To-Do List App',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'A simple to-do list application built with Nuxt.js and Flask' }
      ]
    }
  },
  
  // Configure runtime config for API URL
  runtimeConfig: {
    public: {
      apiBaseUrl: 'https://8000-ibf724rj1lqoxiv9qehks-e80c6714.manus.computer'
    }
  },
  
  // Configure Tailwind CSS
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css',
    configPath: 'tailwind.config.js'
  }
})
