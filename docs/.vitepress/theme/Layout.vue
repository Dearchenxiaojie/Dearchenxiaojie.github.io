<script setup>
import { useData, useRoute } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import { computed, ref, onMounted, onUnmounted } from 'vue'
import HomeLayout from './components/HomeLayout.vue'
import GalleryLayout from './components/GalleryLayout.vue'
import AboutLayout from './components/AboutLayout.vue'
import ToolsLayout from './components/ToolsLayout.vue'
import SavesLayout from './components/SavesLayout.vue'

const { Layout: VitePressLayout } = DefaultTheme
const route = useRoute()

// 初始化主题
function initTheme() {
  const saved = localStorage.getItem("cloudlog-theme")
  if (saved === "dark") {
    document.documentElement.classList.add("dark")
  } else if (saved === "light") {
    document.documentElement.classList.remove("dark")
  } else {
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches
    if (prefersDark) document.documentElement.classList.add("dark")
  }
}

// 阅读进度
const readingProgress = ref(0)
function updateProgress() {
  const scrollTop = window.scrollY
  const docHeight = document.documentElement.scrollHeight - window.innerHeight
  readingProgress.value = docHeight > 0 ? Math.min(scrollTop / docHeight, 1) : 0
}

onMounted(() => {
  initTheme()
  window.addEventListener("scroll", updateProgress)
})

onUnmounted(() => {
  window.removeEventListener("scroll", updateProgress)
})

const pageStyle = computed(() => {
  const path = route.path
  if (path === '/' || path === '/index.html') return 'home'
  if (path.startsWith('/gallery')) return 'gallery'
  if (path.startsWith('/about')) return 'about'
  if (path.startsWith('/tools')) return 'tools'
  if (path.startsWith('/saves')) return 'saves'
  if (path.startsWith('/posts')) return 'posts'
  return 'home'
})
</script>

<template>
  <div class="cloudlog-app" :class="`scene-${pageStyle}`">
    <!-- 阅读进度条 - 仅文章页 -->
    <div v-if="pageStyle === 'posts'" class="reading-progress"
         :style="{ width: readingProgress * 100 + '%' }"></div>
    <!-- 首页：自定义布局 -->
    <HomeLayout v-if="pageStyle === 'home'" />

    <!-- 相册页：自定义布局 -->
    <GalleryLayout v-else-if="pageStyle === 'gallery'" />

    <!-- 关于页：自定义布局 -->
    <AboutLayout v-else-if="pageStyle === 'about'" />

    <!-- 工具页：自定义布局 -->
    <ToolsLayout v-else-if="pageStyle === 'tools'" />

    <!-- 存档页：自定义布局 -->
    <SavesLayout v-else-if="pageStyle === 'saves'" />

    <!-- 文章页和其他：使用 VitePress 默认布局 -->
    <VitePressLayout v-else />

    <!-- 全局音乐播放器 -->
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

/* 深色模式场景背景 */
:root.dark .scene-home {
  background: linear-gradient(135deg, #292524 0%, #1c1917 33%, #292524 66%, #1c1917 100%);
}
:root.dark .scene-posts { background: #0f172a; }
:root.dark .scene-about {
  background: linear-gradient(135deg, #292524 0%, #44403c 50%, #292524 100%);
}

.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--color-primary-500);
  z-index: 10000;
  transition: width 0.1s linear;
  border-radius: 0 2px 2px 0;
}

</style>
