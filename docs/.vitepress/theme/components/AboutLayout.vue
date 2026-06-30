<script setup>
import NavBar from './NavBar.vue'
import Footer from './Footer.vue'
</script>

<template>
  <div class="about-page">
    <NavBar />

    <!-- 背景图 -->
    <div class="about-bg">
      <div class="about-bg-fallback"></div>
      <img src="/images/bg-about.png" alt="" class="about-bg-img" @load="$el.classList.add('loaded')" />
      <div class="about-bg-overlay"></div>
    </div>

    <!-- Hero -->
    <section class="about-hero">
      <div class="about-avatar-wrapper">
        <div class="about-avatar-glow"></div>
        <img src="/avatar.jpg" alt="头像" class="about-avatar-img" />
      </div>
      <h1>关于我</h1>
      <p class="about-name">你好，我是 Dearchenxiaojie 👋</p>
    </section>

    <!-- 内容卡片 -->
    <div class="about-content">
      <section class="about-card">
        <h2>🏠 这是什么地方？</h2>
        <p>这是我的个人博客，一个记录和分享的小天地。在这里我会分享游戏相关、技术折腾、生活记录等内容。这个博客就是我业余做的一个项目，用来记录和分享我感兴趣的东西。</p>
      </section>

      <section class="about-card">
        <h2>🌱 成长历程</h2>
        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <span class="timeline-date">2026.06</span>
              <span class="timeline-text">搭建个人博客，开始记录生活</span>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <span class="timeline-date">2025.09</span>
              <span class="timeline-text">开始学习前端开发</span>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <span class="timeline-date">2025.06</span>
              <span class="timeline-text">接触编程</span>
            </div>
          </div>
        </div>
      </section>

      <section class="about-card">
        <h2>💡 技能 / 兴趣</h2>
        <div class="skills-grid">
          <div class="skill-card">
            <div class="skill-icon">💻</div>
            <h3>编程</h3>
            <ul><li>Python</li><li>C#</li><li>JavaScript</li></ul>
          </div>
          <div class="skill-card">
            <div class="skill-icon">🎨</div>
            <h3>设计</h3>
            <ul><li>网页设计</li><li>UI/UX</li><li>平面设计</li></ul>
          </div>
          <div class="skill-card">
            <div class="skill-icon">🔧</div>
            <h3>其他</h3>
            <ul><li>Minecraft</li><li>摄影</li><li>折腾</li></ul>
          </div>
        </div>
      </section>

      <section class="about-card">
        <h2>📬 联系方式</h2>
        <div class="contact-grid">
          <a href="mailto:2949536466@qq.com" class="contact-card">
            <span class="contact-icon">✉️</span>
            <span class="contact-label">Email</span>
            <span class="contact-value">2949536466@qq.com</span>
          </a>
          <a href="https://github.com/Dearchenxiaojie" target="_blank" class="contact-card">
            <span class="contact-icon">🐙</span>
            <span class="contact-label">GitHub</span>
            <span class="contact-value">Dearchenxiaojie</span>
          </a>
        </div>
      </section>
    </div>

    <Footer />
  </div>
</template>

<style scoped>
.about-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  position: relative;
}

.about-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
}

.about-bg-fallback {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #FFF8F0 0%, #FDE8D0 50%, #F5D5B8 100%);
}

:root.dark .about-bg-fallback {
  background: linear-gradient(135deg, #292524 0%, #44403C 50%, #292524 100%);
}

.about-bg-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.8s ease;
}

.about-bg-img.loaded {
  opacity: 1;
}

.about-bg-overlay {
  position: absolute;
  inset: 0;
  background: rgba(253, 232, 208, 0.82);
}

:root.dark .about-bg-overlay {
  background: rgba(26, 24, 22, 0.88);
}

.about-hero {
  position: relative;
  z-index: 1;
  text-align: center;
  padding: var(--space-16) var(--space-6) var(--space-10);
}

.about-avatar-wrapper {
  position: relative;
  width: 140px;
  height: 140px;
  margin: 0 auto var(--space-6);
}

.about-avatar-glow {
  position: absolute;
  inset: -15px;
  background: radial-gradient(circle, rgba(196,149,106,0.35) 0%, transparent 70%);
  border-radius: 50%;
}

.about-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid var(--bg-card);
  box-shadow: var(--shadow-lg);
  position: relative;
}

.about-hero h1 {
  font-size: 2.5rem;
  margin-bottom: var(--space-3);
}

.about-name {
  color: var(--text-secondary);
  font-size: 1.125rem;
}

.about-content {
  position: relative;
  z-index: 1;
  max-width: 720px;
  margin: 0 auto;
  padding: 0 var(--space-6) var(--space-16);
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.about-card {
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border-radius: var(--radius-xl);
  padding: var(--space-8);
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-sm);
}

.about-card h2 {
  font-size: 1.5rem;
  margin-bottom: var(--space-4);
}

.about-card p {
  color: var(--text-secondary);
  line-height: 1.8;
}

/* 时间线 */
.timeline {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding-left: var(--space-6);
  border-left: 2px solid var(--border-default);
}

.timeline-item {
  position: relative;
  padding-left: var(--space-6);
}

.timeline-dot {
  position: absolute;
  left: calc(-1 * var(--space-6) - 5px);
  top: 4px;
  width: 10px;
  height: 10px;
  background: var(--color-primary);
  border-radius: 50%;
  border: 2px solid var(--bg-card);
}

.timeline-date {
  display: block;
  font-size: 0.8rem;
  color: var(--color-primary);
  font-weight: 600;
  margin-bottom: var(--space-1);
}

.timeline-text {
  color: var(--text-secondary);
  font-size: 0.95rem;
}

/* 技能 */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-4);
}

.skill-card {
  text-align: center;
  padding: var(--space-4);
  background: var(--bg-secondary);
  border-radius: var(--radius-lg);
}

.skill-icon {
  font-size: 2rem;
  margin-bottom: var(--space-2);
}

.skill-card h3 {
  font-size: 1rem;
  margin-bottom: var(--space-2);
}

.skill-card ul {
  list-style: none;
  padding: 0;
}

.skill-card li {
  font-size: 0.85rem;
  color: var(--text-secondary);
  padding: 2px 0;
}

/* 联系方式 */
.contact-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-4);
}

.contact-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-6);
  background: var(--bg-secondary);
  border-radius: var(--radius-lg);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition-fast);
  border: 1px solid transparent;
}

.contact-card:hover {
  border-color: var(--color-primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  color: inherit;
}

.contact-icon {
  font-size: 2rem;
}

.contact-label {
  font-size: 0.8rem;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.contact-value {
  font-size: 0.95rem;
  color: var(--text-primary);
  font-weight: 500;
}

@media (max-width: 768px) {
  .about-hero { padding: var(--space-12) var(--space-4) var(--space-8); }
  .about-hero h1 { font-size: 1.875rem; }
  .skills-grid { grid-template-columns: 1fr; }
  .contact-grid { grid-template-columns: 1fr; }
}
</style>
