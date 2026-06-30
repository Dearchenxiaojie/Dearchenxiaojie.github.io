<script setup>
import { computed } from 'vue'
import { data as posts } from '../posts.data.mjs'
import photosData from '../photos.json'
import NavBar from './NavBar.vue'
import Footer from './Footer.vue'

const recentPosts = posts.slice(0, 3)

// 从 photos.json 获取最新月份的照片
const galleryPhotos = computed(() => {
  const photos = []
  const years = Object.keys(photosData).sort().reverse()
  if (years.length > 0) {
    const latestYear = years[0]
    const months = Object.keys(photosData[latestYear]).sort().reverse()
    if (months.length > 0) {
      const latestMonth = months[0]
      const monthPhotos = photosData[latestYear][latestMonth]
      monthPhotos.slice(0, 6).forEach(filename => {
        photos.push({
          src: `/gallery/${latestYear}/${latestYear}-${latestMonth}/${filename}`,
          alt: `${latestYear}年${parseInt(latestMonth)}月`
        })
      })
    }
  }
  return photos
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
</script>

<template>
  <div class="home-page">
    <!-- 导航栏 -->
    <NavBar />

    <!-- Hero 区域 -->
    <section class="hero">
      <!-- 背景图 -->
      <div class="hero-bg">
        <img src="/images/bg-hero.png" alt="" class="hero-bg-img" />
        <div class="hero-bg-overlay"></div>
      </div>

      <div class="hero-content">
        <div class="hero-text">
          <div class="hero-badge">
            <span class="badge-dot"></span>
            <span>欢迎来到我的小天地</span>
          </div>
          <h1 class="hero-title">
            <span>用数据的思维</span>
            <span class="highlight">记录生活的温度</span>
          </h1>
          <p class="hero-desc">
            你好，我是 Dearchenxiaojie 👋<br>
            热爱折腾 · 喜欢分享 · 记录生活点滴
          </p>
          <div class="hero-actions">
            <a href="/posts/" class="btn btn-primary">查看文章</a>
            <a href="/gallery/" class="btn btn-outline">浏览相册</a>
          </div>
        </div>
        <div class="hero-visual">
          <div class="avatar-wrapper">
            <div class="avatar-glow"></div>
            <img src="/avatar.jpg" alt="头像" class="avatar-img" />
          </div>
        </div>
      </div>
    </section>

    <!-- 最新文章 -->
    <section class="section">
      <div class="section-header">
        <div>
          <span class="section-badge">📝 最新发布</span>
          <h2>近期文章</h2>
          <p class="section-desc">分享学习心得与生活感悟</p>
        </div>
        <a href="/posts/" class="view-all">查看全部 →</a>
      </div>
      <div class="posts-grid">
        <article v-for="post in recentPosts" :key="post.url" class="post-card">
          <a :href="post.url">
            <div class="post-cover">
              <div class="cover-text">{{ post.coverText }}</div>
            </div>
            <div class="post-body">
              <div class="post-meta">
                <time>{{ post.date }}</time>
                <span>{{ post.readingTime }} 分钟阅读</span>
              </div>
              <h3>{{ post.title }}</h3>
              <p>{{ post.description }}</p>
              <div class="post-tags">
                <span v-for="tag in post.tags" :key="tag" class="tag">#{{ tag }}</span>
              </div>
            </div>
          </a>
        </article>
      </div>
    </section>

    <!-- 照片预览 -->
    <section class="section">
      <div class="section-header">
        <div>
          <span class="section-badge">📷 光影瞬间</span>
          <h2>近期拍摄</h2>
          <p class="section-desc">共 {{ totalPhotos }} 张照片</p>
        </div>
        <a href="/gallery/" class="view-all">进入相册 →</a>
      </div>
      <div class="gallery-grid">
        <div v-for="(photo, index) in galleryPhotos" :key="index" class="gallery-item">
          <img
            :src="photo.src"
            :alt="photo.alt"
            loading="lazy"
            decoding="async"
            class="gallery-img"
          />
        </div>
      </div>
    </section>

    <!-- 页脚 -->
    <Footer />
  </div>
</template>

<style scoped>
.home-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Hero 区域 */
.hero {
  position: relative;
  padding: var(--space-20) var(--space-6) var(--space-16);
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.hero-bg-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(250, 250, 248, 0.3) 0%,
    rgba(250, 250, 248, 0.6) 50%,
    rgba(250, 250, 248, 0.95) 100%
  );
}

:root.dark .hero-bg-overlay {
  background: linear-gradient(
    to bottom,
    rgba(26, 24, 22, 0.5) 0%,
    rgba(26, 24, 22, 0.7) 50%,
    rgba(26, 24, 22, 0.95) 100%
  );
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: var(--max-width);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: var(--space-16);
  align-items: center;
}

.hero-text {
  max-width: 560px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background: var(--bg-card);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: var(--space-6);
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: var(--color-primary);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: 3.5rem;
  line-height: 1.2;
  margin-bottom: var(--space-6);
}

.hero-title span {
  display: block;
}

.highlight {
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-light));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-desc {
  font-size: 1.125rem;
  color: var(--text-secondary);
  margin-bottom: var(--space-8);
  line-height: 1.8;
}

.hero-actions {
  display: flex;
  gap: var(--space-4);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-lg);
  font-size: 1rem;
  font-weight: 500;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  color: white;
}

.btn-outline {
  border: 2px solid var(--border-default);
  color: var(--text-primary);
}

.btn-outline:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

/* 头像 */
.hero-visual {
  display: flex;
  justify-content: center;
}

.avatar-wrapper {
  position: relative;
  width: 280px;
  height: 280px;
}

.avatar-glow {
  position: absolute;
  inset: -20px;
  background: radial-gradient(
    circle,
    rgba(196, 149, 106, 0.3) 0%,
    transparent 70%
  );
  border-radius: 50%;
  animation: glow 3s ease-in-out infinite;
}

@keyframes glow {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50% { opacity: 0.8; transform: scale(1.05); }
}

.avatar-img {
  position: relative;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid var(--bg-card);
  box-shadow: var(--shadow-xl);
}

/* 区块通用 */
.section {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--space-16) var(--space-6);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: var(--space-10);
}

.section-badge {
  display: inline-blo
