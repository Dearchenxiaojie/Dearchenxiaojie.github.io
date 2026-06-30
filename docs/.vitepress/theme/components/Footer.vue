<script setup>
// 导航链接
const navLinks = [
  { text: '首页', link: '/' },
  { text: '文章', link: '/posts/' },
  { text: '相册', link: '/gallery/' },
  { text: '关于', link: '/about' },
]

// 社交链接
const socialLinks = [
  { text: 'GitHub', link: 'https://github.com/Dearchenxiaojie' },
  { text: 'Email', link: 'mailto:2949536466@qq.com' },
]
</script>

<template>
  <footer class="site-footer">
    <!-- 云纹过渡 -->
    <div class="footer-cloud-transition">
      <div class="footer-cloud-fallback"></div>
      <img src="/images/bg-footer.png" alt="" class="footer-cloud-img" @load="$el.classList.add('loaded')" />
    </div>

    <div class="footer-content">
      <div class="footer-inner">
        <!-- 品牌区 -->
        <div class="footer-brand">
          <div class="footer-logo">
            <span class="logo-icon">☁️</span>
            <span class="logo-text">云上日志</span>
          </div>
          <p class="footer-desc">用热爱记录每一天</p>
        </div>

        <!-- 链接区 -->
        <div class="footer-links">
          <div class="footer-link-group">
            <h4>导航</h4>
            <a
              v-for="link in navLinks"
              :key="link.link"
              :href="link.link"
            >
              {{ link.text }}
            </a>
          </div>
          <div class="footer-link-group">
            <h4>社交</h4>
            <a
              v-for="link in socialLinks"
              :key="link.link"
              :href="link.link"
              target="_blank"
            >
              {{ link.text }}
            </a>
          </div>
        </div>
      </div>

      <!-- 底部版权 -->
      <div class="footer-bottom">
        <p>© 2026 云上日志 · 用 ❤️ 构建</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  margin-top: auto;
}

/* 云纹过渡 */
.footer-cloud-transition {
  width: 100%;
  height: 120px;
  overflow: hidden;
  line-height: 0;
  position: relative;
}

.footer-cloud-fallback {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, var(--bg-page) 0%, #2D2926 100%);
}

:root.dark .footer-cloud-fallback {
  background: linear-gradient(to bottom, var(--bg-page) 0%, #1A1816 100%);
}

.footer-cloud-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  opacity: 0;
  transition: opacity 0.8s ease;
}

.footer-cloud-img.loaded {
  opacity: 1;
}

/* 页脚内容 */
.footer-content {
  background: #2D2926;
  color: rgba(250, 250, 248, 0.7);
  padding: var(--space-12) 0 0;
}

:root.dark .footer-content {
  background: #1A1816;
}

.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  display: flex;
  justify-content: space-between;
  gap: var(--space-12);
}

/* 品牌区 */
.footer-brand {
  max-width: 280px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}

.footer-logo .logo-icon {
  font-size: 1.75rem;
}

.footer-logo .logo-text {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 600;
  color: rgba(250, 250, 248, 0.9);
}

.footer-desc {
  font-size: 0.9rem;
  color: rgba(250, 250, 248, 0.5);
  margin: 0;
}

/* 链接区 */
.footer-links {
  display: flex;
  gap: var(--space-12);
}

.footer-link-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer-link-group h4 {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(250, 250, 248, 0.4);
  margin-bottom: var(--space-2);
}

.footer-link-group a {
  color: rgba(250, 250, 248, 0.7);
  font-size: 0.9rem;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-link-group a:hover {
  color: var(--color-primary-light);
}

/* 底部版权 */
.footer-bottom {
  margin-top: var(--space-10);
  padding: var(--space-6);
  border-top: 1px solid rgba(250, 250, 248, 0.1);
  text-align: center;
}

.footer-bottom p {
  color: rgba(250, 250, 248, 0.4);
  font-size: 0.85rem;
  margin: 0;
}

/* 响应式 */
@media (max-width: 768px) {
  .footer-cloud-transition {
    height: 80px;
  }

  .footer-inner {
    flex-direction: column;
    gap: var(--space-8);
  }

  .footer-brand {
    max-width: 100%;
  }

  .footer-links {
    gap: var(--space-8);
  }
}
</style>
