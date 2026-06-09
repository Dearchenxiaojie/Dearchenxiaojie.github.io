<script setup>
</script>

<template>
  <div class="gallery-page">
    <!-- 导航栏（深色版） -->
    <nav class="gallery-nav">
      <div class="nav-inner">
        <a href="/" class="nav-logo">☁️ 云上日志</a>
        <ul class="nav-links">
          <li><a href="/">首页</a></li>
          <li><a href="/posts/">文章</a></li>
          <li><a href="/gallery/" class="active">相册</a></li>
          <li><a href="/about">关于</a></li>
        </ul>
      </div>
    </nav>

    <!-- 标题区 -->
    <section class="gallery-hero">
      <h1>「每一帧都是限定版的时光」</h1>
      <div class="gallery-filters">
        <span class="filter active">全部</span>
        <span class="filter">🏫 校园</span>
        <span class="filter">✈️ 旅行</span>
        <span class="filter">🍜 美食</span>
        <span class="filter">📷 日常</span>
      </div>
    </section>

    <!-- 瀑布流照片墙 -->
    <section class="gallery-wall">
      <div class="masonry-grid">
        <div class="photo-item" v-for="i in 8" :key="i">
          <div class="photo-placeholder">
            <span>{{ ['🌸','☀️','🍂','❄️','📷','🌙','🌿','✨'][i-1] }}</span>
          </div>
          <div class="photo-overlay">
            <p class="photo-title">照片标题 {{ i }}</p>
            <p class="photo-date">2026.06.{{ 9 - i }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 照片故事卡片（示例） -->
    <div class="photo-story-modal">
      <div class="story-card">
        <div class="story-image">📷</div>
        <div class="story-content">
          <h3>「照片标题」</h3>
          <p>这张照片背后的故事...</p>
          <div class="story-meta">
            <span>📍 地点</span>
            <span>📅 2026年6月9日</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
