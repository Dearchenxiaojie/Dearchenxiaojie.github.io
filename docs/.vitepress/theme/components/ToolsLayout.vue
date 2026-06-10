<script setup>
const tools = [
  {
    icon: '🎮',
    name: 'PCL2 启动器',
    desc: 'Plain Craft Launcher 2 - 我的 Minecraft 启动器',
    link: 'https://afdian.net/a/LTCat',
    tags: ['游戏', 'Minecraft']
  },
  {
    icon: '🐙',
    name: 'GitHub',
    desc: '全球最大的代码托管平台',
    link: 'https://github.com',
    tags: ['开发', '代码']
  },
  {
    icon: '💻',
    name: 'VS Code',
    desc: '微软出品的免费代码编辑器',
    link: 'https://code.visualstudio.com',
    tags: ['开发', '编辑器']
  },
  {
    icon: '🚀',
    name: 'Watt Toolkit',
    desc: '免费开源的 GitHub 加速工具',
    link: 'https://steampp.net',
    tags: ['网络', '加速']
  }
]
</script>

<template>
  <div class="tools-page">
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
          <a href="/tools/" class="menu-item active">工具</a>
          <a href="/saves/" class="menu-item">存档</a>
          <a href="/about" class="menu-item">关于</a>
        </nav>
      </div>
    </header>

    <section class="tools-hero">
      <h1>🔧 工具推荐</h1>
      <p>我日常使用的好用工具和软件</p>
    </section>

    <section class="tools-content">
      <div class="tools-grid">
        <a v-for="tool in tools" :key="tool.name" :href="tool.link" target="_blank" class="tool-card">
          <div class="tool-icon">{{ tool.icon }}</div>
          <div class="tool-info">
            <h3>{{ tool.name }}</h3>
            <p>{{ tool.desc }}</p>
            <div class="tool-tags">
              <span v-for="tag in tool.tags" :key="tag" class="tag">#{{ tag }}</span>
            </div>
          </div>
          <div class="tool-arrow">→</div>
        </a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.tools-page {
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

.tools-hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 5rem 1.5rem 3rem;
  text-align: center;
}
.tools-hero h1 {
  font-family: var(--font-serif);
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
.tools-hero p {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.tools-content {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1.5rem 4rem;
}
.tools-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.tool-card {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem;
  background: var(--bg-card);
  border-radius: var(--radius-xl);
  border: 1px solid var(--border-light);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition-base);
}
.tool-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary-200);
}
.tool-icon {
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
.tool-info {
  flex: 1;
}
.tool-info h3 {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}
.tool-info p {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 0.75rem;
}
.tool-tags {
  display: flex;
  gap: 0.5rem;
}
.tag {
  padding: 0.25rem 0.75rem;
  background: var(--color-primary-100);
  color: var(--color-primary-700);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
}
.tool-arrow {
  font-size: 1.5rem;
  color: var(--text-tertiary);
  transition: transform var(--transition-fast);
}
.tool-card:hover .tool-arrow {
  transform: translateX(4px);
  color: var(--color-primary-500);
}

@media (max-width: 768px) {
  .navbar-menu { display: none; }
  .tools-hero { padding: 3rem 1rem 2rem; }
  .tools-hero h1 { font-size: 1.75rem; }
}
</style>
