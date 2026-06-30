<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import photosData from '../photos.json'
import NavBar from './NavBar.vue'
import Footer from './Footer.vue'

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
        name: filename
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

// 灯箱状态
const lbOpen = ref(false)
const lbIndex = ref(0)

const allPhotos = computed(() => {
  const list = []
  months.value.forEach(m => m.photos.forEach(p => list.push(p)))
  return list
})

function openLB(i) { lbIndex.value = i; lbOpen.value = true }
function closeLB() { lbOpen.value = false }
function prevLB() { if (lbIndex.value > 0) lbIndex.value-- }
function nextLB() { if (lbIndex.value < allPhotos.value.length - 1) lbIndex.value++ }
function onKey(e) {
  if (!lbOpen.value) return
  if (e.key === "Escape") closeLB()
  if (e.key === "ArrowLeft") prevLB()
  if (e.key === "ArrowRight") nextLB()
}
onMounted(() => window.addEventListener("keydown", onKey))
onUnmounted(() => window.removeEventListener("keydown", onKey))

// 计算月份偏移量，用于灯箱全局索引
const monthOffsets = computed(() => {
  let offset = 0
  return months.value.map(m => {
    const result = offset
    offset += m.photos.length
    return result
  })
})

// 主题切换
function toggleTheme() {
  document.documentElement.classList.toggle('dark')
  localStorage.setItem('cloudlog-theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light')
}
</script>

<template>
  <div class="gallery-page">
    <NavBar />

    <!-- 背景图 -->
    <div class="gallery-bg">
      <div class="gallery-bg-fallback"></div>
      <img src="/images/bg-gallery.png" alt="" class="gallery-bg-img" @load="$el.classList.add('loaded')" />
      <div class="gallery-bg-overlay"></div>
    </div>

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
      <div v-for="(monthData, monthIndex) in months" :key="monthData.month" class="month-section">
        <div class="month-header">
          <h2>{{ activeYear }}年{{ monthData.label }}</h2>
          <span class="photo-count">{{ monthData.photos.length }} 张</span>
        </div>

        <div class="photo-grid">
          <div
            v-for="(photo, index) in monthData.photos"
            :key="photo.name"
            class="photo-card"
            @click="openLB(index + (monthOffsets[monthIndex] || 0))"
          >
            <img
              :src="photo.src"
              :alt="photo.name"
              decoding="async"
              class="photo-img"
              @error="$el.src = $el.src"
            />
          </div>
        </div>
      </div>
    </section>

    <Footer />

    <!-- 灯箱 -->
    <Teleport to="body">
      <div v-if="lbOpen" class="lightbox-overlay" @click.self="closeLB">
        <button class="lightbox-close" @click="closeLB">✕</button>
        <button v-if="lbIndex > 0" class="lightbox-nav lightbox-prev" @click="prevLB">‹</button>
        <div class="lightbox-content">
          <img :src="allPhotos[lbIndex].src" :alt="allPhotos[lbIndex].name" class="lightbox-image" />
          <p class="lightbox-caption">{{ allPhotos[lbIndex].name }}</p>
        </div>
        <button v-if="lbIndex < allPhotos.length - 1" class="lightbox-nav lightbox-next" @click="nextLB">›</button>
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
.gallery-page {
  min-height: 100vh;
  background: #0F0F1A;
  color: #E8E6E3;
  position: relative;
}

/* 背景图 */
.gallery-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
}

.gallery-bg-fallback {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, #0F0F23 0%, #1A1A2E 50%, #0F0F1A 100%);
}

.gallery-bg-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.8s ease;
}

.gallery-bg-img.loaded {
  opacity: 1;
}

.gallery-bg-overlay {
  position: absolute;
  inset: 0;
  background: rgba(15, 15, 26, 0.7);
}

/* Hero */
.gallery-hero {
  position: relative;
  z-index: 1;
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
  transition: transform var(--transition-base);
  cursor: pointer;
  position: relative;
}

.photo-card:hover {
  transform: scale(1.05);
}

.photo-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 灯箱 */
.lightbox-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(0, 0, 0, 0.95);
  display: flex;
  align-items: center;
  justify-content: center;
}
.lightbox-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  font-size: 1.25rem;
  border: none;
  cursor: pointer;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.2);
}
.lightbox-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  font-size: 2rem;
  border: none;
  cursor: pointer;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.lightbox-nav:hover {
  background: rgba(255, 255, 255, 0.2);
}
.lightbox-prev {
  left: 1.5rem;
}
.lightbox-next {
  right: 1.5rem;
}
.lightbox-content {
  max-width: 90vw;
  max-height: 85vh;
  text-align: center;
}
.lightbox-image {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 0.5rem;
}
.lightbox-caption {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.875rem;
  margin-top: 0.75rem;
}

/* 响应式 */
@media (max-width: 768px) {
  .gallery-hero {
    padding: 3rem 1rem 2rem;
  }
  .gallery-hero h1 {
    font-size: 1.75rem;
  }
  .photo-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}

/* 确保内容在背景图之上 */
.gallery-content,
.gallery-hero {
  position: relative;
  z-index: 1;
}
</style>
