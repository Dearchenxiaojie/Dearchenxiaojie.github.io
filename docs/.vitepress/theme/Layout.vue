<script setup>
import { useData, useRoute } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import { computed } from 'vue'
import HomeLayout from './components/HomeLayout.vue'
import GalleryLayout from './components/GalleryLayout.vue'
import AboutLayout from './components/AboutLayout.vue'
import MusicPlayer from './components/MusicPlayer.vue'

const { Layout: VitePressLayout } = DefaultTheme
const route = useRoute()

const pageStyle = computed(() => {
  const path = route.path
  if (path === '/' || path === '/index.html') return 'home'
  if (path.startsWith('/gallery')) return 'gallery'
  if (path.startsWith('/about')) return 'about'
  if (path.startsWith('/posts')) return 'posts'
  return 'home'
})
</script>

<template>
  <div class="cloudlog-app" :class="`scene-${pageStyle}`">
    <!-- 首页：自定义布局 -->
    <HomeLayout v-if="pageStyle === 'home'" />

    <!-- 相册页：自定义布局 -->
    <GalleryLayout v-else-if="pageStyle === 'gallery'" />

    <!-- 关于页：自定义布局 -->
    <AboutLayout v-else-if="pageStyle === 'about'" />

    <!-- 文章页和其他：使用 VitePress 默认布局 -->
    <VitePressLayout v-else />

    <!-- 全局音乐播放器 -->
    <MusicPlayer />
  </div>
</template>

<style scoped>
.cloudlog-app {
  min-height: 100vh;
  transition: background 0.5s ease;
}

/* 首页：大融合 - 暖白底 */
.scene-home {
  background: linear-gradient(135deg, #FFF5F7 0%, #F0F8FF 33%, #FFF8F0 66%, #F5F7FA 100%);
}

/* 文章页：冬·书房 - 冰蓝白 */
.scene-posts {
  background: #F5F7FA;
}

/* 相册页：夜·展厅 - 深蓝黑 */
.scene-gallery {
  background: #0F0F23;
  color: #E8E6E3;
}

/* 关于页：秋·咖啡馆 - 奶茶色 */
.scene-about {
  background: linear-gradient(135deg, #FFF8F0 0%, #FDE8D0 50%, #F5D5B8 100%);
}
</style>
