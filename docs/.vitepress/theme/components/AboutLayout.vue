<script setup>
</script>

<template>
  <div class="about-page">
    <!-- 导航栏 -->
    <header class="navbar">
      <div class="navbar-inner">
        <a href="/" class="navbar-logo">
          <span class="logo-icon">☁️</span>
          <span class="logo-text">云上日志</span>
        </a>

        <nav class="navbar-menu" aria-label="主导航">
          <a href="/" class="menu-item">首页</a>
          <a href="/posts/" class="menu-item">文章</a>
          <a href="/gallery/" class="menu-item">相册</a>
          <a href="/about" class="menu-item active">关于</a>
                  <button
  class="theme-toggle"
  onclick="document.documentElement.classList.toggle('dark');localStorage.setItem('cloudlog-theme',document.documentElement.classList.contains('dark')?'dark':'light')"
  aria-label="切换主题"
>🌓</button>
        </nav>
      </div>
    </header>

    <!-- Hero 区域 -->
    <section class="about-hero">
      <div class="about-avatar">👤</div>
      <h1>关于我</h1>
      <p class="about-name">你好，我是 Dearchenxiaojie 👋</p>
    </section>

    <!-- 关于我 -->
    <section class="about-card">
      <h2>关于我</h2>
      <p>一个喜欢折腾的人。喜欢研究各种有趣的工具和软件，也喜欢把好用的东西分享给大家。这个博客就是我业余做的一个项目，用来记录和分享我感兴趣的东西。</p>
    </section>

    <!-- 成长历程 -->
    <section class="about-card">
      <h2>成长历程</h2>
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

    <!-- 技能 / 兴趣 -->
    <section class="about-card">
      <h2>技能 / 兴趣</h2>
      <div class="skills-grid">
        <div class="skill-card">
          <div class="skill-icon">💻</div>
          <h3>编程</h3>
          <ul class="skill-list">
            <li>Python</li>
            <li>C#</li>
            <li>JavaScript</li>
          </ul>
        </div>
        <div class="skill-card">
          <div class="skill-icon">🎨</div>
          <h3>设计</h3>
          <ul class="skill-list">
            <li>网页设计</li>
            <li>UI/UX</li>
            <li>平面设计</li>
          </ul>
        </div>
        <div class="skill-card">
          <div class="skill-icon">🔧</div>
          <h3>其他</h3>
          <ul class="skill-list">
            <li>Minecraft</li>
            <li>游戏</li>
            <li>折腾</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 联系方式 -->
    <section class="about-card">
      <h2>联系方式</h2>
      <div class="contact-grid">
        <a href="mailto:2949536466@qq.com" class="contact-card">
          <span class="contact-icon">✉️</span>
          <span class="contact-label">Email</span>
        </a>
        <a href="https://github.com/Dearchenxiaojie" target="_blank" class="contact-card">
          <span class="contact-icon">🐙</span>
          <span class="contact-label">GitHub</span>
        </a>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="about-footer">
      <p>© 2026 云上日志 · 用热爱记录每一天</p>
    </footer>
  </div>
</template>

<style scoped>
.theme-toggle {
  background: none; border: none;
  font-size: 1.125rem; cursor: pointer;
  padding: 0.25rem; border-radius: var(--radius-md);
  line-height: 1; margin-left: 0.5rem;
  transition: background var(--transition-fast);
}
.theme-toggle:hover { background: var(--bg-tertiary); }
</style>
