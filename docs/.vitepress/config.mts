import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '云上日志',
  description: '数据在云上，生活在日志里',
  lang: 'zh-CN',

  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#C4956A' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: '云上日志' }],
    ['meta', { property: 'og:description', content: '数据在云上，生活在日志里' }],
  ],

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: '云上日志',

    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/posts/' },
      { text: '相册', link: '/gallery/' },
      { text: '工具', link: '/tools/' },
      { text: '存档', link: '/saves/' },
      { text: '关于', link: '/about' },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Dearchenxiaojie' }
    ],

    footer: {
      message: '用热爱记录每一天',
      copyright: '© 2026 云上日志'
    },

    search: {
      provider: 'local'
    }
  }
})
