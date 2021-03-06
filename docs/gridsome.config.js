// This is where project configuration and plugin options are located. 
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

module.exports = {
  siteName: 'NBody Simulations',
  icon: {
    favicon: './src/assets/favicon.png',
    touchicon: './src/assets/favicon.png'
  },
  siteUrl: 'https://sparxastronomy.github.io/nbody',
  settings: {
    web: 'https://github.com/sparxastronomy/' || true,
    twitter: process.env.URL_TWITTER || false,
    github: 'https://github.com/sparxastronomy/Nbody' || true,
    nav: {
      links: [
        { path: '/docs/', title: 'Docs' }
      ]
    },
    sidebar: [
      {
        name: 'docs',
        sections: [
          {
            title: 'Getting Started',
            items: [
              '/docs/',
              '/docs/installation/'
            ]
          },
          {
            title: 'Simple N Body Simulations',
            items: [
              '/docs/3d/intro/',
              '/docs/3d/science/',
              '/docs/3d/example/'
            ]
          },
          {
            title: 'Advance N Body Simulations',
            items: [
              '/docs/2d/intro/',
              '/docs/2d/science/'
            ]
          }
        ]
      }
    ]
  },
  plugins: [
    {
      use: '@gridsome/source-filesystem',
      options: {
        baseDir: './content',
        path: '**/*.md',
        typeName: 'MarkdownPage',
        remark: {
          externalLinksTarget: '_blank',
          externalLinksRel: ['noopener', 'noreferrer'],
          plugins: [
            '@gridsome/remark-prismjs',
            'gridsome-remark-katex'
          ]
        }
      }
    },

    {
      use: 'gridsome-plugin-tailwindcss',
      options: {
        tailwindConfig: './tailwind.config.js',
        purgeConfig: {
          // Prevent purging of prism classes.
          whitelistPatternsChildren: [
            /token$/
          ]
        }
      }
    },

    {
      use: '@gridsome/plugin-google-analytics',
      options: {
        id: (process.env.GA_ID ? process.env.GA_ID : 'G-8STNTT705S')
      }
    },

    {
      use: '@gridsome/plugin-sitemap',
      options: {
      }
    }

  ],
  transformers: {
    remark: {
      plugins: [
        ['gridsome-remark-katex', { minRuleThickness: 0.1, fontSize: 1.3 }]
      ]
    }
  }
}
