<script setup>
</script>

<template>
  <div class="about-page">
    <!-- 导航栏 -->
    <nav class="about-nav">
      <div class="nav-inner">
        <a href="/" class="nav-logo">☁️ 云上日志</a>
        <ul class="nav-links">
          <li><a href="/">首页</a></li>
          <li><a href="/posts/">文章</a></li>
          <li><a href="/gallery/">相册</a></li>
          <li><a href="/about" class="active">关于</a></li>
        </ul>
      </div>
    </nav>

    <!-- 个人介绍头部 -->
    <section class="about-hero">
      <div class="about-avatar">
        <div class="avatar-placeholder">📷</div>
      </div>
      <h1>你好呀 👋</h1>
      <p class="about-name">我是 Dearchenxiaojie，很高兴认识你</p>
    </section>

    <!-- 关于我 -->
    <section class="about-card">
      <h2>关于我</h2>
      <p>「我是一个大数据专业的学生，喜欢用代码解决问题，也喜欢用镜头记录生活。这个博客是我的小天地，记录那些值得被记住的瞬间。」</p>
    </section>

    <!-- 时间线 -->
    <section class="about-card">
      <h2>我的时间线</h2>
      <div class="timeline">
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2026.06</span>
            <span class="timeline-text">创建了「云上日志」博客</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2025.09</span>
            <span class="timeline-text">开始学习大数据</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2024.06</span>
            <span class="timeline-text">高中毕业</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <span class="timeline-date">2023.xx</span>
            <span class="timeline-text">写下第一行代码</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 技能/兴趣 -->
    <section class="about-card">
      <h2>技能 / 兴趣</h2>
      <div class="skills-grid">
        <div class="skill-card">
          <div class="skill-icon">💻</div>
          <h3>编程</h3>
          <ul>
            <li>Python</li>
            <li>C#</li>
            <li>JavaScript</li>
          </ul>
        </div>
        <div class="skill-card">
          <div class="skill-icon">📷</div>
          <h3>摄影</h3>
          <ul>
            <li>风景</li>
            <li>人像</li>
            <li>后期</li>
          </ul>
        </div>
        <div class="skill-card">
          <div class="skill-icon">📖</div>
          <h3>阅读</h3>
          <ul>
            <li>技术</li>
            <li>文学</li>
            <li>写作</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 联系方式 -->
    <section class="about-card">
      <h2>联系方式</h2>
      <div class="contact-links">
        <a href="mailto:2949536466@qq.com" class="contact-btn">
          <span class="contact-icon">📧</span>
          <span>Email</span>
        </a>
        <a href="https://github.com/Dearchenxiaojie" target="_blank" class="contact-btn">
          <span class="contact-icon">🐙</span>
          <span>GitHub</span>
        </a>
      </div>
    </section>

    <!-- 页脚 -->
    <footer class="about-footer">
      <p>© 2026 云上日志 · 用 ❤️ 构建</p>
    </footer>
  </div>
</template>
