/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'pythonbible',
  tagline: '',
  url: 'https://docs.python.bible',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'avendesora', // Usually your GitHub org/user name.
  projectName: 'pythonbible', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'pythonbible',
      // logo: {
      //   alt: 'My Site Logo',
      //   src: 'img/logo.svg',
      // },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'How-To and Reference Docs',
        },
        // {
        //   type: 'doc',
        //   docId: 'reference',
        //   position: 'left',
        //   label: 'Reference',
        // },
        // {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/avendesora/pythonbible',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      // links: [
      //   {
      //     title: 'Docs',
      //     items: [
      //       {
      //         label: 'Tutorial',
      //         to: '/docs/intro',
      //       },
      //     ],
      //   },
      //   // {
      //   //   title: 'Community',
      //   //   items: [
      //   //     {
      //   //       label: 'Stack Overflow',
      //   //       href: 'https://stackoverflow.com/questions/tagged/docusaurus',
      //   //     },
      //   //     {
      //   //       label: 'Discord',
      //   //       href: 'https://discordapp.com/invite/docusaurus',
      //   //     },
      //   //     {
      //   //       label: 'Twitter',
      //   //       href: 'https://twitter.com/docusaurus',
      //   //     },
      //   //   ],
      //   // },
      //   {
      //     title: 'More',
      //     items: [
      //       // {
      //       //   label: 'Blog',
      //       //   to: '/blog',
      //       // },
      //       {
      //         label: 'GitHub',
      //         href: 'https://github.com/avendesora/pythonbible',
      //       },
      //     ],
      //   },
      // ],
      copyright: `Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/avendesora/pythonbible/edit/main/pythonbible-docs/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/avendesora/pythonbible/edit/main/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
