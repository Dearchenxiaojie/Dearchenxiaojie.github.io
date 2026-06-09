<script setup>
import { useData } from 'vitepress'
import { data as posts } from '../posts.data.mjs'

const { site, frontmatter } = useData()

const recentPosts = posts.slice(0, 3)
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
          <a href="/about" class="menu-item">关于</a>
        </nav>

        <div class="navbar-actions">
          <button class="search-btn" aria-label="搜索">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <path d="m21 21-4.35-4.35"></path>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- Hero 区域 -->
    <section class="hero">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="badge-dot"></span>
          <span>欢迎来到我的小天地</span>
        </div>

        <h1 class="hero-title">
          <span class="title-line">用数据的思维</span>
          <span class="title-line highlight">记录生活的温度</span>
        </h1>

        <p class="hero-description">
          你好，我是 Dearchenxiaojie 👋<br>
          大数据专业 · 生活记录者 · 摄影爱好者
        </p>

        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-number">{{ posts.length }}</span>
            <span class="stat-label">篇文章</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-number">0</span>
            <span class="stat-label">张照片</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-number">3</span>
            <span class="stat-label">个标签</span>
          </div>
        </div>

        <div class="hero-actions">
          <a href="/posts/" class="btn btn-primary">
            <span>探索文章</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="m9 18 6-6-6-6"></path>
            </svg>
          </a>
          <a href="/about" class="btn btn-outline">了解更多</a>
        </div>
      </div>

      <div class="hero-visual">
        <div class="visual-card">
          <div class="card-placeholder">
            <span class="placeholder-emoji">✨</span>
            <span class="placeholder-text">记录美好瞬间</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 最新文章 -->
    <section class="section posts-section">
      <div class="section-header">
        <div>
          <span class="section-badge">📝 最新发布</span>
          <h2 class="section-title">近期文章</h2>
          <p class="section-desc">分享学习心得与生活感悟</p>
        </div>
        <a href="/posts/" class="view-all-link">
          查看全部
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="m9 18 6-6-6-6"></path>
          </svg>
        </a>
      </div>

      <div class="posts-grid">
        <article v-for="post in recentPosts" :key="post.url" class="post-card">
          <a :href="post.url" class="post-card-link">
            <div class="post-cover">
              <div class="cover-gradient"></div>
              <span class="cover-emoji">📝</span>
            </div>
            <div class="post-content">
              <div class="post-meta">
                <time class="post-date">{{ post.date }}</time>
                <span class="post-reading">{{ post.readingTime }} 分钟阅读</span>
              </div>
              <h3 class="post-title">{{ post.title }}</h3>
              <p class="post-excerpt">{{ post.description }}</p>
              <div class="post-tags">
                <span v-for="tag in post.tags" :key="tag" class="tag">#{{ tag }}</span>
              </div>
            </div>
          </a>
        </article>
      </div>
    </section>

    <!-- 照片预览 -->
    <section class="section gallery-section">
      <div class="section-header">
        <div>
          <span class="section-badge">📷 光影瞬间</span>
          <h2 class="section-title">近期拍摄</h2>
          <p class="section-desc">用镜头记录生活中的美好</p>
        </div>
        <a href="/gallery/" class="view-all-link">
          进入相册
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="m9 18 6-6-6-6"></path>
          </svg>
        </a>
      </div>

      <div class="gallery-preview">
        <div class="gallery-grid">
          <div class="gallery-item large">
            <div class="gallery-placeholder">
              <span>🌸</span>
            </div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">
              <span>☀️</span>
            </div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">
              <span>🍂</span>
            </div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">
              <span>❄️</span>
            </div>
          </div>
          <div class="gallery-item">
            <div class="gallery-placeholder">
              <span>🌙</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 代码角落 -->
    <section class="section code-section">
      <div class="section-header">
        <div>
          <span class="section-badge">💻 代码角落</span>
          <h2 class="section-title">最近的代码片段</h2>
          <p class="section-desc">用代码解决问题的乐趣</p>
        </div>
      </div>

      <div class="code-block">
        <div class="code-header">
          <div class="code-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <span class="code-filename">life.py</span>
          <button class="copy-btn">复制</button>
        </div>
        <pre class="code-content"><code>from datetime import datetime

class Life:
    """记录生活的类"""
    def __init__(self):
        self.mood = "😊"
        self.today = "写了一个爬虫"
        self.date = datetime.now()

    def log(self):
        return f"{self.date}: {self.mood} {self.today}"

# 记录今天
me = Life()
print(me.log())</code></pre>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-brand">
          <span class="footer-logo">☁️</span>
          <span class="footer-name">云上日志</span>
          <p class="footer-tagline">用热爱记录每一天</p>
        </div>

        <div class="footer-links">
          <div class="footer-column">
            <h4>导航</h4>
            <a href="/">首页</a>
            <a href="/posts/">文章</a>
            <a href="/gallery/">相册</a>
            <a href="/about">关于</a>
          </div>
          <div class="footer-column">
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
/* ========== 导航栏 ========== */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 250, 245, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-light);
  height: var(--nav-height);
}

.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  text-decoration: none;
  color: var(--text-primary);
}

.logo-icon {
  font-size: 24px;
}

.logo-text {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 600;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: var(--space-8);
}

.menu-item {
  color: var(--text-secondary);
  font-size: var(--text-sm);
  font-weight: 500;
  text-decoration: none;
  padding: var(--space-2) 0;
  position: relative;
  transition: color var(--transition-fast);
}

.menu-item:hover,
.menu-item.active {
  color: var(--text-primary);
}

.menu-item.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-primary);
  border-radius: 1px;
}

.search-btn {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  transition: all var(--transition-fast);
}

.search-btn:hover {
  background: var(--bg-secondary);
  color: var(--text-primary);
}

/* ========== Hero 区域 ========== */
.hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--space-24) var(--space-6) var(--space-16);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-16);
  align-items: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  background: var(--color-primary-lightest);
  color: var(--color-primary);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: 500;
  margin-bottom: var(--space-6);
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: var(--color-primary);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: var(--text-5xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  margin-bottom: var(--space-6);
}

.title-line {
  display: block;
}

.title-line.highlight {
  background: linear-gradient(135deg, var(--color-primary), var(--color-primary-lighter));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: var(--text-lg);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-8);
}

.hero-stats {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  margin-bottom: var(--space-8);
  padding: var(--space-6);
  background: var(--bg-card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-light);
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
}

.stat-number {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--color-primary);
}

.stat-label {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: var(--border-default);
}

.hero-actions {
  display: flex;
  gap: var(--space-4);
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-lg);
  font-size: var(--text-base);
  font-weight: 500;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.btn-primary {
  background: var(--color-primary);
  color: var(--text-inverse);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
  color: var(--text-inverse);
}

.btn-outline {
  background: transparent;
  color: var(--text-primary);
  border: 2px solid var(--border-default);
}

.btn-outline:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.hero-visual {
  display: flex;
  justify-content: center;
}

.visual-card {
  width: 100%;
  max-width: 400px;
  aspect-ratio: 4/3;
  background: linear-gradient(135deg, var(--color-primary-lightest), var(--bg-secondary));
  border-radius: var(--radius-2xl);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-light);
}

.card-placeholder {
  text-align: center;
}

.placeholder-emoji {
  font-size: 64px;
  display: block;
  margin-bottom: var(--space-4);
}

.placeholder-text {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  color: var(--color-primary);
}

/* ========== 区块通用 ========== */
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
  display: inline-block;
  padding: var(--space-1) var(--space-3);
  background: var(--bg-tertiary);
  color: var(--color-primary);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: 500;
  margin-bottom: var(--space-3);
}

.section-title {
  font-family: var(--font-serif);
  font-size: var(--text-3xl);
  font-weight: 700;
  margin-bottom: var(--space-2);
}

.section-desc {
  color: var(--text-secondary);
  font-size: var(--text-base);
}

.view-all-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  color: var(--color-primary);
  font-size: var(--text-sm);
  font-weight: 500;
  text-decoration: none;
  transition: gap var(--transition-fast);
}

.view-all-link:hover {
  gap: var(--space-2);
}

/* ========== 文章卡片网格 ========== */
.posts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-8);
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
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--border-default);
}

.post-card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.post-cover {
  position: relative;
  height: 200px;
  background: linear-gradient(135deg, var(--color-primary-lightest), var(--bg-secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.cover-gradient {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(139, 105, 20, 0.1), rgba(218, 165, 32, 0.1));
}

.cover-emoji {
  font-size: 48px;
  position: relative;
  z-index: 1;
}

.post-content {
  padding: var(--space-6);
}

.post-meta {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  margin-bottom: var(--space-3);
  font-size: var(--text-sm);
  color: var(--text-tertiary);
}

.post-date {
  font-weight: 500;
}

.post-title {
  font-family: var(--font-serif);
  font-size: var(--text-xl);
  font-weight: 600;
  line-height: var(--leading-snug);
  margin-bottom: var(--space-3);
  color: var(--text-primary);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-excerpt {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-4);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.tag {
  padding: var(--space-1) var(--space-3);
  background: var(--bg-tertiary);
  color: var(--color-primary);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: 500;
}

/* ========== 相册预览 ========== */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 200px);
  gap: var(--space-4);
}

.gallery-item {
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--bg-tertiary);
  transition: transform var(--transition-base);
}

.gallery-item:hover {
  transform: scale(1.02);
}

.gallery-item.large {
  grid-column: span 2;
  grid-row: span 2;
}

.gallery-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--color-primary-lightest), var(--bg-secondary));
}

.gallery-placeholder span {
  font-size: 48px;
}

.gallery-item.large .gallery-placeholder span {
  font-size: 64px;
}

/* ========== 代码块 ========== */
.code-block {
  max-width: 600px;
  margin: 0 auto;
  background: var(--bg-code);
  border-radius: var(--radius-xl);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
}

.code-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-4) var(--space-5);
  background: #21252B;
}

.code-dots {
  display: flex;
  gap: 6px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot.red { background: #FF5F56; }
.dot.yellow { background: #FFBD2E; }
.dot.green { background: #27C93F; }

.code-filename {
  color: #636D83;
  font-size: var(--text-sm);
  font-family: var(--font-mono);
  flex: 1;
}

.copy-btn {
  padding: var(--space-1) var(--space-3);
  background: rgba(255, 255, 255, 0.1);
  color: #636D83;
  border-radius: var(--radius-sm);
  font-size: var(--text-xs);
  transition: all var(--transition-fast);
}

.copy-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: #ABB2BF;
}

.code-content {
  padding: var(--space-5);
  margin: 0;
  background: transparent;
}

.code-content code {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  color: #ABB2BF;
  background: none;
  padding: 0;
}

/* ========== 页脚 ========== */
.footer {
  background: var(--color-black);
  color: var(--text-inverse);
  padding: var(--space-16) 0 0;
  margin-top: var(--space-16);
}

.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: flex;
  justify-content: space-between;
  gap: var(--space-16);
}

.footer-brand {
  max-width: 300px;
}

.footer-logo {
  font-size: 32px;
  display: block;
  margin-bottom: var(--space-3);
}

.footer-name {
  font-family: var(--font-display);
  font-size: var(--text-2xl);
  font-weight: 600;
  display: block;
  margin-bottom: var(--space-2);
}

.footer-tagline {
  color: rgba(255, 255, 255, 0.6);
  font-size: var(--text-sm);
}

.footer-links {
  display: flex;
  gap: var(--space-16);
}

.footer-column {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer-column h4 {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255, 255, 255, 0.4);
  margin-bottom: var(--space-2);
}

.footer-column a {
  color: rgba(255, 255, 255, 0.8);
  font-size: var(--text-sm);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-column a:hover {
  color: var(--color-primary-lighter);
}

.footer-bottom {
  margin-top: var(--space-12);
  padding: var(--space-6);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.footer-bottom p {
  color: rgba(255, 255, 255, 0.4);
  font-size: var(--text-sm);
  margin: 0;
}

/* ========== 响应式 ========== */
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    gap: var(--space-10);
    padding: var(--space-16) var(--space-6) var(--space-10);
  }

  .hero-visual {
    display: none;
  }

  .posts-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .navbar-menu {
    display: none;
  }

  .hero {
    padding: var(--space-10) var(--space-4) var(--space-8);
  }

  .hero-title {
    font-size: var(--text-4xl);
  }

  .hero-stats {
    flex-direction: row;
    justify-content: space-around;
    padding: var(--space-4);
  }

  .stat-divider {
    width: 40px;
    height: 1px;
  }

  .hero-actions {
    flex-direction: column;
  }

  .btn {
    justify-content: center;
  }

  .section {
    padding: var(--space-10) var(--space-4);
  }

  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--space-4);
  }

  .posts-grid {
    grid-template-columns: 1fr;
  }

  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: auto;
  }

  .gallery-item.large {
    grid-column: span 2;
    grid-row: span 1;
  }

  .footer-inner {
    flex-direction: column;
    gap: var(--space-10);
  }

  .footer-links {
    gap: var(--space-10);
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: var(--text-3xl);
  }

  .gallery-grid {
    grid-template-columns: 1fr;
  }

  .gallery-item.large {
    grid-column: span 1;
  }
}
</style>
