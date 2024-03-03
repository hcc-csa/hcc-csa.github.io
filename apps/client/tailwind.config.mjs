/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      width: {
        400: '400px'
      },
      height: {
        400: '400px'
      },
      backdropBlur: {
        '5xl': '250px'
      }
    },
    backgroundSize: {
      '75%': '75%'
    }
  },
  plugins: []
}
