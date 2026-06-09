<script setup>
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
          <a href="/about" class="menu-item">关于</a>
        </nav>
      </div>
    </header>

    <!-- Hero 区域 -->
    <section class="gallery-hero">
      <h1>「每一帧都是限定版的时光」</h1>
      <div class="gallery-filters">
        <button class="filter-btn active">全部</button>
        <button class="filter-btn">🏫 校园</button>
        <button class="filter-btn">✈️ 旅行</button>
        <button class="filter-btn">🍜 美食</button>
        <button class="filter-btn">📷 日常</button>
      </div>
    </section>

    <!-- 瀑布流照片墙 -->
    <section class="gallery-wall">
      <div class="masonry-grid">
        <div class="photo-card" v-for="i in 8" :key="i">
          <div class="photo-placeholder">
            <span>{{ ['🌸','☀️','🍂','❄️','📷','🌙','🌿','✨'][i-1] }}</span>
          </div>
          <div class="photo-overlay">
            <p class="photo-title">照片标题 {{ i }}</p>
            <div class="photo-meta">
              <span class="photo-date">2026.06.{{ 9 - i }}</span>
              <span class="photo-location">📍 地点</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 照片故事卡片示例 -->
    <div class="photo-story-modal">
      <button class="story-close">✕</button>
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
