/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/templates/**/*.jinja",
    "./app/python/**/*.py",
    "./static/src/**/*.{html,js,css}",
    "./templates/**/*.{html,js}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
