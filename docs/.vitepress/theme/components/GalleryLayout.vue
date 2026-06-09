<script setup>
import { ref, onMounted } from 'vue'

// 照片数据（按年月分类）
const photoGroups = ref([
  {
    year: '2025',
    months: [
      { month: '09', label: '9月', photos: 7 },
      { month: '08', label: '8月', photos: 10 },
      { month: '07', label: '7月', photos: 2 },
      { month: '06', label: '6月', photos: 21 },
      { month: '01', label: '1月', photos: 5 },
    ]
  },
  {
    year: '2024',
    months: [
      { month: '09', label: '9月', photos: 1 },
      { month: '08', label: '8月', photos: 7 },
      { month: '06', label: '6月', photos: 2 },
      { month: '03', label: '3月', photos: 12 },
      { month: '02', label: '2月', photos: 2 },
      { month: '01', label: '1月', photos: 2 },
    ]
  },
  {
    year: '2023',
    months: [
      { month: '12', label: '12月', photos: 1 },
      { month: '11', label: '11月', photos: 4 },
      { month: '08', label: '8月', photos: 1 },
      { month: '06', label: '6月', photos: 2 },
      { month: '05', label: '5月', photos: 1 },
      { month: '04', label: '4月', photos: 1 },
    ]
  }
])

const activeYear = ref('2025')
const activeMonth = ref(null)

const setActive = (year, month) => {
  activeYear.value = year
  activeMonth.value = month
}

const getPhotoUrl = (year, month, index) => {
  return `/gallery/${year}/${year}-${month}/IMG_${year}${month}*.jpg`
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
      <p class="gallery-desc">共 81 张照片 · 记录生活中的美好瞬间</p>
      <div class="gallery-filters">
        <button
          v-for="group in photoGroups"
          :key="group.year"
          class="filter-btn"
          :class="{ active: activeYear === group.year && !activeMonth }"
          @click="activeYear = group.year; activeMonth = null"
        >
          {{ group.year }}年
        </button>
      </div>
    </section>

    <!-- 按月分组展示 -->
    <section class="gallery-content">
      <div v-for="group in photoGroups" :key="group.year" v-show="activeYear === group.year">
        <div v-for="monthData in group.months" :key="monthData.month" class="month-section">
          <div class="month-header">
            <h2>{{ group.year }}年{{ monthData.label }}</h2>
            <span class="photo-count">{{ monthData.photos }} 张</span>
          </div>

          <div class="photo-grid">
            <div
              v-for="i in monthData.photos"
              :key="i"
              class="photo-card"
            >
              <div class="photo-placeholder">
                <span class="photo-icon">📷</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 提示 -->
    <section class="gallery-note">
      <p>💡 照片已按年月分类存放在 <code>/gallery/</code> 目录下</p>
    </section>
  </div>
</template>

<style scoped>
.gallery-page {
  min-height: 100vh;
  background: #0F0F1A;
  color: #E8E6E3;
}

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

.photo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}
.photo-card {
  aspect-ratio: 1;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: linear-gradient(135deg, #1A1A2E, #16213E);
  transition: transform var(--transition-base);
  cursor: pointer;
}
.photo-card:hover {
  transform: scale(1.05);
}
.photo-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.photo-icon {
  font-size: 2rem;
  opacity: 0.5;
}

.gallery-note {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 2rem 1.5rem;
  text-align: center;
}
.gallery-note p {
  color: rgba(255, 255, 255, 0.4);
  font-size: 0.875rem;
}
.gallery-note code {
  background: rgba(255, 255, 255, 0.1);
  padding: 0.25rem 0.5rem;
  border-radius: var(--radius-sm);
  color: var(--color-primary-400);
}

@media (max-width: 768px) {
  .navbar-menu { display: none; }
  .gallery-hero { padding: 3rem 1rem 2rem; }
  .gallery-hero h1 { font-size: 1.75rem; }
  .photo-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
}
</style>
