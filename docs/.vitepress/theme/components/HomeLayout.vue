<script setup>
import { useData } from 'vitepress'
import { ref } from 'vue'
import { data as posts } from '../posts.data.mjs'

const { site, frontmatter } = useData()
const recentPosts = posts.slice(0, 3)

// 根据文章标签返回图标
const getPostIcon = (tags) => {
  if (!tags || tags.length === 0) return '📝'
  const tag = tags[0].toLowerCase()
  if (tag.includes('github') || tag.includes('git')) return '🐙'
  if (tag.includes('工具') || tag.includes('软件')) return '🔧'
  if (tag.includes('教程') || tag.includes('指南')) return '📚'
  if (tag.includes('游戏') || tag.includes('minecraft')) return '🎮'
  if (tag.includes('代码') || tag.includes('编程')) return '💻'
  if (tag.includes('生活') || tag.includes('日常')) return '🌿'
  return '📝'
}
</script>

<template>
  <div class="home-page">
    <!-- 导航栏 -->
    <header class="navbar">
      <div class="navbar-inner">
        <a href="/" class="navbar-logo">
          <span class="logo-icon">☁️</span>
          <span class="logo-text">云上日志</span>
        </a>
        <nav class="navbar-menu">
          <a href="/" class="menu-item active">首页</a>
          <a href="/posts/" class="menu-item">文章</a>
          <a href="/gallery/" class="menu-item">相册</a>
          <a href="/tools/" class="menu-item">工具</a>
          <a href="/saves/" class="menu-item">存档</a>
          <a href="/about" class="menu-item">关于</a>
        </nav>
      </div>
    </header>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-content">
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
        <div class="visual-card">
          <img src="/avatar.jpg" alt="头像" class="avatar-img" />
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
              <img v-if="post.cover" :src="post.cover" :alt="post.title" loading="lazy" decoding="async" />
              <span v-else>{{ getPostIcon(post.tags) }}</span>
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
          <p class="section-desc">用镜头记录生活中的美好</p>
        </div>
        <a href="/gallery/" class="view-all">进入相册 →</a>
      </div>
      <div class="gallery-grid">
        <div class="gallery-item large">
          <img src="/gallery/2025/2025-06/IMG_20250615_131559.jpg" alt="2025年6月" loading="lazy" decoding="async" />
        </div>
        <div class="gallery-item">
          <img src="/gallery/2025/2025-06/IMG_20250615_131708.jpg" alt="2025年6月" loading="lazy" decoding="async" />
        </div>
        <div class="gallery-item">
          <img src="/gallery/2025/2025-06/IMG_20250615_131802.jpg" alt="2025年6月" loading="lazy" decoding="async" />
        </div>
        <div class="gallery-item">
          <img src="/gallery/2025/2025-06/IMG_20250615_131935.jpg" alt="2025年6月" loading="lazy" decoding="async" />
        </div>
        <div class="gallery-item">
          <img src="/gallery/2025/2025-06/IMG_20250615_132557.jpg" alt="2025年6月" loading="lazy" decoding="async" />
        </div>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-brand">
          <span class="footer-logo">☁️</span>
          <span class="footer-name">云上日志</span>
          <p>用热爱记录每一天</p>
        </div>
        <div class="footer-links">
          <div>
            <h4>导航</h4>
            <a href="/">首页</a>
            <a href="/posts/">文章</a>
            <a href="/gallery/">相册</a>
            <a href="/about">关于</a>
          </div>
          <div>
            <h4>社交</h4>
            <a href="https://github.com/Dearchenxiaojie" target="_blank">GitHub</a>
            <a href="mailto:2949536466@qq.com">Email</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 云上日志 · 用 ❤️ 构建</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
/* 导航栏 */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(250, 250, 249, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-light);
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
  color: var(--text-primary);
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
}
.navbar-menu {
  display: flex;
  gap: 2rem;
}
.menu-item {
  color: var(--text-secondary);
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
}
.menu-item:hover, .menu-item.active {
  color: var(--text-primary);
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
.hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 6rem 1.5rem 4rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  background: linear-gradient(135deg, var(--color-primary-50) 0%, var(--bg-primary) 50%, var(--autumn-50) 100%);
  border-radius: var(--radius-2xl);
  margin-top: 2rem;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.375rem 1rem;
  background: var(--color-primary-100);
  color: var(--color-primary-800);
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}
.badge-dot {
  width: 0.5rem;
  height: 0.5rem;
  background: var(--color-primary-500);
  border-radius: 50%;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
.hero-title {
  font-size: 3rem;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}
.hero-title span {
  display: block;
}
.highlight {
  background: linear-gradient(135deg, var(--color-primary-600), var(--color-primary-400));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-desc {
  font-size: 1.125rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
}
.hero-actions {
  display: flex;
  gap: 1rem;
}
.btn {
  display: inline-flex;
  align-items: center;
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-lg);
  font-size: 1rem;
  font-weight: 500;
  transition: all var(--transition-fast);
}
.btn-primary {
  background: var(--color-primary-600);
  color: white;
}
.btn-primary:hover {
  background: var(--color-primary-700);
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  color: white;
}
.btn-outline {
  border: 2px solid var(--border-default);
  color: var(--text-primary);
}
.btn-outline:hover {
  border-color: var(--color-primary-400);
  color: var(--color-primary-700);
}
.hero-visual {
  display: flex;
  justify-content: center;
}
.visual-card {
  width: 100%;
  max-width: 24rem;
  aspect-ratio: 4/3;
  background: linear-gradient(135deg, var(--color-primary-100), var(--color-primary-50));
  border-radius: var(--radius-2xl);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  box-shadow: var(--shadow-lg);
  overflow: hidden;
}
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 区块 */
.section {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 4rem 1.5rem;
}
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2.5rem;
}
.section-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
}
.section-desc {
  color: var(--text-secondary);
  font-size: 1rem;
}
.view-all {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-primary-600);
}

/* 文章卡片 */
.posts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}
.post-card {
  background: var(--bg-card);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-light);
  transition: all var(--transition-base);
}
.post-card:hover {
  transform: translateY(-0.25rem);
  box-shadow: var(--shadow-lg);
}
.post-card a {
  color: inherit;
  display: block;
}
.post-cover {
  height: 12rem;
  background: linear-gradient(135deg, var(--color-primary-100), var(--bg-secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  overflow: hidden;
}
.post-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.post-body {
  padding: 1.5rem;
}
.post-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.875rem;
  color: var(--text-tertiary);
  margin-bottom: 0.75rem;
}
.post-body h3 {
  font-size: 1.25rem;
  margin-bottom: 0.75rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.post-body p {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tag {
  padding: 0.25rem 0.75rem;
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 500;
}

/* 相册预览 - 瀑布流 */
.gallery-grid {
  columns: 3;
  column-gap: 12px;
}
.gallery-item {
  break-inside: avoid;
  margin-bottom: 12px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: transform var(--transition-base);
  cursor: pointer;
}
.gallery-item:hover {
  transform: scale(1.02);
}
.gallery-item img {
  width: 100%;
  height: auto;
  display: block;
}

/* 代码块 */
.code-block {
  max-width: 36rem;
  margin: 0 auto;
  background: var(--bg-code);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
}
.code-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: var(--color-stone-950);
}
.code-dots {
  display: flex;
  gap: 0.375rem;
}
.dot {
  width: 0.75rem;
  height: 0.75rem;
  border-radius: 50%;
}
.dot.red { background: #ef4444; }
.dot.yellow { background: #eab308; }
.dot.green { background: #22c55e; }
.code-filename {
  color: var(--color-stone-400);
  font-size: 0.875rem;
  font-family: var(--font-mono);
  flex: 1;
}
.copy-btn {
  padding: 0.25rem 0.75rem;
  background: rgba(255,255,255,0.1);
  color: var(--color-stone-400);
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
}
.code-block pre {
  margin: 0;
  padding: 1.25rem;
  background: transparent;
}

/* 页脚 */
.footer {
  background: var(--color-stone-900);
  color: var(--text-inverse);
  padding: 4rem 0 0;
  margin-top: 4rem;
}
.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  justify-content: space-between;
  gap: 4rem;
}
.footer-brand {
  max-width: 18rem;
}
.footer-logo {
  font-size: 2rem;
  display: block;
  margin-bottom: 0.75rem;
}
.footer-name {
  font-family: var(--font-display);
  font-size: 1.5rem;
  display: block;
  margin-bottom: 0.5rem;
}
.footer-brand p {
  color: rgba(255,255,255,0.6);
  font-size: 0.875rem;
}
.footer-links {
  display: flex;
  gap: 4rem;
}
.footer-links div {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.footer-links h4 {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255,255,255,0.4);
  margin-bottom: 0.5rem;
}
.footer-links a {
  color: rgba(255,255,255,0.8);
  font-size: 0.875rem;
}
.footer-links a:hover {
  color: var(--color-primary-400);
}
.footer-bottom {
  margin-top: 3rem;
  padding: 1.5rem;
  border-top: 1px solid rgba(255,255,255,0.1);
  text-align: center;
}
.footer-bottom p {
  color: rgba(255,255,255,0.4);
  font-size: 0.875rem;
}

/* 响应式 */
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .hero-visual { display: none; }
  .posts-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
  .navbar-menu { display: none; }
  .hero { padding: 3rem 1rem 2rem; }
  .hero-title { font-size: 2rem; }
  .hero-stats { flex-direction: row; justify-content: space-around; padding: 1rem; }
  .stat-divider { width: 2.5rem; height: 1px; }
  .hero-actions { flex-direction: column; }
  .btn { justify-content: center; }
  .posts-grid { grid-template-columns: 1fr; }
  .gallery-grid { grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; }
  .gallery-item.large { grid-column: span 2; grid-row: span 1; }
  .footer-inner { flex-direction: column; gap: 2.5rem; }
}
</style>
