import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import Layout from './Layout.vue'
import './styles/global.css'
import './styles/animations.css'

export default {
  extends: DefaultTheme,
  Layout
} satisfies Theme
