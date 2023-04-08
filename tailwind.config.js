const defaultTheme = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#1B73E8',
      },
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
      fontSize: {
        sm: ['14px', '17px'],
        base: ['16px', '130%'],
        lg: ['20px', '130%'],
        xl: ['24px', '32px'],
      },
    },
  },
  plugins: [],
};
