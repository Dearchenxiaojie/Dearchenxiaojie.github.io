<script setup>
import NavBar from './NavBar.vue'
import Footer from './Footer.vue'

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
    <NavBar />

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

    <Footer />
  </div>
</template>

<style scoped>
.saves-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-page);
}

.saves-hero {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: var(--space-16) var(--space-6) var(--space-10);
  text-align: center;
}

.saves-hero h1 {
  font-size: 2.5rem;
  margin-bottom: var(--space-3);
}

.saves-hero p {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.saves-content {
  max-width: 720px;
  margin: 0 auto;
  padding: 0 var(--space-6) var(--space-16);
}

.saves-grid {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.save-card {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  padding: var(--space-5) var(--space-6);
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: var(--radius-xl);
  border: 1px solid var(--border-light);
}

.save-icon {
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

:root.dark .save-icon {
  background: rgba(196, 149, 106, 0.12);
}

.save-info {
  flex: 1;
}

.save-info h3 {
  font-size: 1.125rem;
  margin-bottom: var(--space-1);
}

.save-info p {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: var(--space-2);
}

.save-count {
  font-size: 0.75rem;
  color: var(--color-primary);
  font-weight: 500;
}

.save-tags {
  display: flex;
  gap: var(--space-2);
  margin-top: var(--space-3);
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

@media (max-width: 768px) {
  .saves-hero { padding: var(--space-12) var(--space-4) var(--space-8); }
  .saves-hero h1 { font-size: 1.875rem; }
}
</style>
