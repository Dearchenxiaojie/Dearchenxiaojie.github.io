<script setup>
import NavBar from './NavBar.vue'
import Footer from './Footer.vue'

const tools = [
  {
    icon: '🎮',
    name: 'PCL2 启动器',
    desc: 'Plain Craft Launcher 2 - 简洁好用的 Minecraft 启动器',
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
    <NavBar />

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

    <Footer />
  </div>
</template>

<style scoped>
.tools-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-page);
}

.tools-hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--space-16) var(--space-6) var(--space-10);
  text-align: center;
}

.tools-hero h1 {
  font-size: 2.5rem;
  margin-bottom: var(--space-3);
}

.tools-hero p {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.tools-content {
  max-width: 720px;
  margin: 0 auto;
  padding: 0 var(--space-6) var(--space-16);
}

.tools-grid {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.tool-card {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  padding: var(--space-5) var(--space-6);
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: var(--radius-xl);
  border: 1px solid var(--border-light);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition-base);
}

.tool-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary);
  color: inherit;
}

.tool-icon {
  font-size: 2.25rem;
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-primary-50);
  border-radius: var(--radius-lg);
  flex-shrink: 0;
}

:root.dark .tool-icon {
  background: rgba(196, 149, 106, 0.12);
}

.tool-info {
  flex: 1;
}

.tool-info h3 {
  font-size: 1.125rem;
  margin-bottom: var(--space-1);
}

.tool-info p {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: var(--space-2);
}

.tool-tags {
  display: flex;
  gap: var(--space-2);
}

.tag {
  padding: 2px 10px;
  background: var(--color-primary-50);
  color: var(--color-primary-700);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 500;
}

:root.dark .tag {
  background: rgba(196, 149, 106, 0.15);
  color: var(--color-primary-light);
}

.tool-arrow {
  font-size: 1.25rem;
  color: var(--text-tertiary);
  transition: transform var(--transition-fast);
}

.tool-card:hover .tool-arrow {
  transform: translateX(4px);
  color: var(--color-primary);
}

@media (max-width: 768px) {
  .tools-hero { padding: var(--space-12) var(--space-4) var(--space-8); }
  .tools-hero h1 { font-size: 1.875rem; }
}
</style>
