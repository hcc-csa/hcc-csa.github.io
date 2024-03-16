/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      flexBasis: {
        '22.5/100': '22.5%'
      },
      width: {
        400: '400px',
        300: '300px',
        '75%': '75%'
      },
      height: {
        400: '400px',
        300: '300px'
      },
      backdropBlur: {
        '4xl': '100px',
        '5xl': '200px',
        '7xl': '250px'
      },
      boxShadow: {
        csa: '0 0 15px 0px rgba(58, 178, 178, 0.2)'
      },
      dropShadow: {
        csa: '0 0 15px 0px rgba(58, 178, 178, 0.2)'
      }
    },
    backgroundSize: {
      '100%': '100%',
      '75%': '75%',
      '50%': '50%'
    }
  },
  plugins: []
}
