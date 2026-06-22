<script setup>
const saves = [
  {
    icon: '🎮',
    name: 'Minecraft 存档',
    desc: '我的 Minecraft 游戏存档分享',
    count: '待添加',
    tags: ['Minecraft', '游戏']
  }
]
</script>

<template>
  <div class="saves-page">
    <header class="navbar">
      <div class="navbar-inner">
        <a href="/" class="navbar-logo">
          <span class="logo-icon">☁️</span>
          <span class="logo-text">云上日志</span>
        </a>
        <nav class="navbar-menu">
          <a href="/" class="menu-item">首页</a>
          <a href="/posts/" class="menu-item">文章</a>
          <a href="/gallery/" class="menu-item">相册</a>
          <a href="/tools/" class="menu-item">工具</a>
          <a href="/saves/" class="menu-item active">存档</a>
          <a href="/about" class="menu-item">关于</a>
                  <button
  class="theme-toggle"
  onclick="document.documentElement.classList.toggle('dark');localStorage.setItem('cloudlog-theme',document.documentElement.classList.contains('dark')?'dark':'light')"
  aria-label="??????"
>??</button>
        </nav>
      </div>
    </header>

    <section class="saves-hero">
      <h1>🎮 存档分享</h1>
      <p>我的游戏存档和地图</p>
    </section>

    <section class="saves-content">
      <div class="saves-grid">
        <div v-for="save in saves" :key="save.name" class="save-card">
          <div class="save-icon">{{ save.icon }}</div>
          <div class="save-info">
            <h3>{{ save.name }}</h3>
            <p>{{ save.desc }}</p>
            <span class="save-count">{{ save.count }}</span>
            <div class="save-tags">
              <span v-for="tag in save.tags" :key="tag" class="tag">#{{ tag }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.saves-page {
  min-height: 100vh;
  background: var(--bg-primary);
}

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

.saves-hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 5rem 1.5rem 3rem;
  text-align: center;
}
.saves-hero h1 {
  font-family: var(--font-serif);
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
.saves-hero p {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.saves-content {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1.5rem 4rem;
}
.saves-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.save-card {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem;
  background: var(--bg-card);
  border-radius: var(--radius-xl);
  border: 1px solid var(--border-light);
}
.save-icon {
  font-size: 2.5rem;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-50);
  border-radius: var(--radius-lg);
  flex-shrink: 0;
}
.save-info {
  flex: 1;
}
.save-info h3 {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}
.save-info p {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
}
.save-count {
  font-size: 0.75rem;
  color: var(--color-primary-500);
  font-weight: 500;
}
.save-tags {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.75rem;
}
.tag {
  padding: 0.25rem 0.75rem;
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
}

@media (max-width: 768px) {
  .navbar-menu { display: none; }
  .saves-hero { padding: 3rem 1rem 2rem; }
  .saves-hero h1 { font-size: 1.75rem; }
}

.theme-toggle {
  background: none; border: none;
  font-size: 1.125rem; cursor: pointer;
  padding: 0.25rem; border-radius: var(--radius-md);
  line-height: 1; margin-left: 0.5rem;
  transition: background var(--transition-fast);
}
.theme-toggle:hover { background: var(--bg-tertiary); }

</style>
