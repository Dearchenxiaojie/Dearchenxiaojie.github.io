<script setup>
import { useData } from 'vitepress'
import { data as posts } from '../posts.data.mjs'

const { site, frontmatter } = useData()

const recentPosts = posts.slice(0, 3)
</script>

<template>
  <div class="home-page">
    <!-- 导航栏 -->
    <nav class="home-nav">
      <div class="nav-inner">
        <a href="/" class="nav-logo">☁️ 云上日志</a>
        <ul class="nav-links">
          <li><a href="/" class="active">首页</a></li>
          <li><a href="/posts/">文章</a></li>
          <li><a href="/gallery/">相册</a></li>
          <li><a href="/about">关于</a></li>
        </ul>
      </div>
    </nav>

    <!-- 个人介绍区 -->
    <section class="hero-section">
      <div class="hero-avatar">
        <div class="avatar-placeholder">📷</div>
      </div>
      <h1 class="hero-title">你好，我是 Dearchenxiaojie 👋</h1>
      <p class="hero-subtitle">大数据专业 · 生活记录者 · 摄影爱好者</p>
      <p class="hero-quote">「用数据的思维，记录生活的温度」</p>

      <div class="hero-stats">
        <div class="stat-card">
          <span class="stat-num">{{ posts.length }}</span>
          <span class="stat-label">篇文章</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">0</span>
          <span class="stat-label">张照片</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">3</span>
          <span class="stat-label">个标签</span>
        </div>
      </div>
    </section>

    <!-- 最新文章 -->
    <section class="section-posts">
      <div class="section-header">
        <h2>📝 最新文章</h2>
        <a href="/posts/" class="view-all">查看全部 →</a>
      </div>

      <div class="posts-grid">
        <a v-for="post in recentPosts" :key="post.url" :href="post.url" class="post-card">
          <div class="post-cover">
            <div class="cover-placeholder">📝</div>
          </div>
          <div class="post-info">
            <h3 class="post-title">{{ post.title }}</h3>
            <p class="post-desc">{{ post.description }}</p>
            <div class="post-meta">
              <span class="post-date">{{ post.date }}</span>
              <span class="post-reading">阅读 {{ post.readingTime }} 分钟</span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- 照片预览 -->
    <section class="section-gallery-preview">
      <div class="section-header">
        <h2>📷 光影瞬间</h2>
        <a href="/gallery/" class="view-all">进入相册 →</a>
      </div>

      <div class="gallery-preview-grid">
        <div class="gallery-placeholder">
          <div class="ph-item">🌸</div>
          <div class="ph-item">☀️</div>
          <div class="ph-item">🍂</div>
          <div class="ph-item">❄️</div>
          <div class="ph-item large">📷</div>
          <div class="ph-item">🌙</div>
        </div>
      </div>
    </section>

    <!-- 代码角落 -->
    <section class="section-code">
      <div class="section-header">
        <h2>💻 代码角落</h2>
      </div>

      <div class="code-block">
        <div class="code-header">
          <div class="code-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <span class="code-filename">life.py</span>
          <span class="code-lang">Python</span>
        </div>
        <pre class="code-content"><code>from datetime import datetime

class Life:
    def __init__(self):
        self.mood = "😊"
        self.today = "写了一个爬虫"
        self.date = datetime.now()

me = Life()
print(f"{me.date}: {me.mood} {me.today}")</code></pre>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="home-footer">
      <p class="footer-logo">☁️ 云上日志</p>
      <p class="footer-desc">用热爱记录每一天</p>
      <div class="footer-links">
        <a href="https://github.com/Dearchenxiaojie" target="_blank">GitHub</a>
        <a href="/feed.xml">RSS</a>
      </div>
      <p class="footer-copy">© 2026 云上日志</p>
    </footer>
  </div>
</template>
