<script setup>
import { ref, computed, onMounted } from 'vue'
import photosData from '../photos.json'

// 处理照片数据
const years = Object.keys(photosData).sort().reverse()
const activeYear = ref(years[0] || '2025')

// 当前年份的月份列表
const months = computed(() => {
  const yearData = photosData[activeYear.value] || {}
  return Object.keys(yearData)
    .sort()
    .reverse()
    .map(month => ({
      month,
      label: `${parseInt(month)}月`,
      photos: yearData[month].map(filename => ({
        src: `/gallery/${activeYear.value}/${activeYear.value}-${month}/${filename}`,
        name: filename,
        loaded: false
      }))
    }))
})

// 总照片数
const totalPhotos = computed(() => {
  let count = 0
  Object.values(photosData).forEach(yearData => {
    Object.values(yearData).forEach(monthPhotos => {
      count += monthPhotos.length
    })
  })
  return count
})

// 加载状态 - 优化：立即显示页面，不阻塞
const isLoading = ref(false)  // 改为 false，不显示加载提示
const loadedCount = ref(0)

// 图片加载完成回调 - 静默处理
const onImageLoad = () => {
  loadedCount.value++
}
</script>

<template>
  <div class="gallery-page">
    <!-- 导航栏 -->
    <header class="navbar">
      <div class="navbar-inner">
        <a href="/" class="navbar-logo">
          <span class="logo-icon">☁️</span>
          <span class="logo-text">云上日志</span>
        </a>
        <nav class="navbar-menu">
          <a href="/" class="menu-item">首页</a>
          <a href="/posts/" class="menu-item">文章</a>
          <a href="/gallery/" class="menu-item active">相册</a>
          <a href="/tools/" class="menu-item">工具</a>
          <a href="/saves/" class="menu-item">存档</a>
          <a href="/about" class="menu-item">关于</a>
        </nav>
      </div>
    </header>

    <!-- Hero -->
    <section class="gallery-hero">
      <h1>「每一帧都是限定版的时光」</h1>
      <p class="gallery-desc">共 {{ totalPhotos }} 张照片 · 记录生活中的美好瞬间</p>
      <div class="gallery-filters">
        <button
          v-for="year in years"
          :key="year"
          class="filter-btn"
          :class="{ active: activeYear === year }"
          @click="activeYear = year"
        >
          {{ year }}年
        </button>
      </div>
    </section>

    <!-- 照片列表 -->
    <section class="gallery-content">
      <div v-for="monthData in months" :key="monthData.month" class="month-section">
        <div class="month-header">
          <h2>{{ activeYear }}年{{ monthData.label }}</h2>
          <span class="photo-count">{{ monthData.photos.length }} 张</span>
        </div>

        <div class="photo-grid">
          <div
            v-for="(photo, index) in monthData.photos"
            :key="photo.name"
            class="photo-card"
            :class="{ 'is-loaded': photo.loaded }"
          >
            <div class="photo-placeholder" v-if="!photo.loaded">
              <div class="photo-spinner"></div>
            </div>
            <img
              :src="photo.src"
              :alt="photo.name"
              loading="lazy"
              decoding="async"
              class="photo-img"
              @load="photo.loaded = true; onImageLoad()"
            />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.gallery-page {
  min-height: 100vh;
  background: #0F0F1A;
  color: #E8E6E3;
}

/* 导航栏 */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(15, 15, 26, 0.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  height: var(--nav-height);
}
.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.navbar-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
}
.navbar-menu {
  display: flex;
  gap: 2rem;
}
.menu-item {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
}
.menu-item:hover, .menu-item.active {
  color: white;
}
.menu-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-primary-500);
  border-radius: 1px;
}

/* Hero */
.gallery-hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 5rem 1.5rem 3rem;
  text-align: center;
}
.gallery-hero h1 {
  font-family: var(--font-display);
  font-size: 2.5rem;
  font-weight: 400;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #FFD700, #FFA500);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.gallery-desc {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 2rem;
}
.gallery-filters {
  display: flex;
  justify-content: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.filter-btn {
  padding: 0.5rem 1.25rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-full);
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  cursor: pointer;
  transition: all var(--transition-fast);
}
.filter-btn:hover, .filter-btn.active {
  background: var(--color-primary-500);
  border-color: var(--color-primary-500);
  color: white;
}

/* 照片内容区 */
.gallery-content {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1.5rem 4rem;
}
.month-section {
  margin-bottom: 3rem;
}
.month-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.month-header h2 {
  font-family: var(--font-serif);
  font-size: 1.5rem;
  color: white;
}
.photo-count {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.5);
}

/* 照片网格 */
.photo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}
.photo-card {
  aspect-ratio: 1;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: #1A1A2E;
  transition: transform var(--transition-base), opacity 0.5s ease;
  cursor: pointer;
  position: relative;
  opacity: 0;
}

.photo-card.is-loaded {
  opacity: 1;
}

.photo-card:hover {
  transform: scale(1.05);
}

/* 照片占位符 */
.photo-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #1A1A2E, #16213E);
}

.photo-spinner {
  width: 32px;
  height: 32px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-top-color: #FFD700;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.photo-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 响应式 */
@media (max-width: 768px) {
  .navbar-menu { display: none; }
  .gallery-hero { padding: 3rem 1rem 2rem; }
  .gallery-hero h1 { font-size: 1.75rem; }
  .photo-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }

  .loading-sidebar {
    width: 260px;
    padding: 1.5rem;
  }
}
</style>
