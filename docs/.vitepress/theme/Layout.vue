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

// 阅读进度
const readingProgress = ref(0)
function updateProgress() {
  const scrollTop = window.scrollY
  const docHeight = document.documentElement.scrollHeight - window.innerHeight
  readingProgress.value = docHeight > 0 ? Math.min(scrollTop / docHeight, 1) : 0
}

onMounted(() => {
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
  <div class="cloudlog-app">
    <!-- 阅读进度条 -->
    <div v-if="pageStyle === 'posts'" class="reading-progress"
         :style="{ width: readingProgress * 100 + '%' }"></div>

    <HomeLayout v-if="pageStyle === 'home'" />
    <GalleryLayout v-else-if="pageStyle === 'gallery'" />
    <AboutLayout v-else-if="pageStyle === 'about'" />
    <ToolsLayout v-else-if="pageStyle === 'tools'" />
    <SavesLayout v-else-if="pageStyle === 'saves'" />
    <VitePressLayout v-else />
  </div>
</template>

<style scoped>
.cloudlog-app {
  min-height: 100vh;
}

.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--color-primary);
  z-index: 10000;
  transition: width 0.1s linear;
  border-radius: 0 2px 2px 0;
}
</style>
