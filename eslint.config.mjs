import withNuxt from './.nuxt/eslint.config.mjs'

export default withNuxt(
  {
    ignores: [
      // Vendored assets and generated output from the previous static site.
      'theme/**',
      'feeds/**',
      'sitemap.xml'
    ]
  }
)
