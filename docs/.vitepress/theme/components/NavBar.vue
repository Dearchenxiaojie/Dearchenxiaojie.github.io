<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()
const mobileMenuOpen = ref(false)
const isDark = ref(false)

// 导航链接
const navLinks = [
  { text: '首页', link: '/' },
  { text: '文章', link: '/posts/' },
  { text: '相册', link: '/gallery/' },
  { text: '工具', link: '/tools/' },
  { text: '存档', link: '/saves/' },
  { text: '关于', link: '/about' },
]

// 判断当前页面
function isActive(link) {
  const path = route.path
  if (link === '/') {
    return path === '/' || path === '/index.html'
  }
  return path.startsWith(link)
}

// 初始化主题
function initTheme() {
  const saved = localStorage.getItem('cloudlog-theme')
  if (saved === 'dark') {
    isDark.value = true
    document.documentElement.classList.add('dark')
  } else if (saved === 'light') {
    isDark.value = false
    document.documentElement.classList.remove('dark')
  } else {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    isDark.value = prefersDark
    if (prefersDark) {
      document.documentElement.classList.add('dark')
    }
  }
}

// 切换主题
function toggleTheme() {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle('dark')
  localStorage.setItem('cloudlog-theme', isDark.value ? 'dark' : 'light')
}

// 切换移动菜单
function toggleMobileMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

// 关闭移动菜单
function closeMobileMenu() {
  mobileMenuOpen.value = false
}

onMounted(() => {
  initTheme()
})
</script>

<template>
  <header class="navbar">
    <div class="navbar-inner">
      <a href="/" class="navbar-logo">
        <span class="logo-icon">☁️</span>
        <span class="logo-text">云上日志</span>
      </a>

      <!-- 桌面导航 -->
      <nav class="navbar-menu" aria-label="主导航">
        <a
          v-for="link in navLinks"
          :key="link.link"
          :href="link.link"
          class="menu-item"
          :class="{ active: isActive(link.link) }"
        >
          {{ link.text }}
        </a>
        <button
          class="theme-toggle"
          @click="toggleTheme"
          :aria-label="isDark ? '切换到浅色模式' : '切换到深色模式'"
        >
          {{ isDark ? '☀️' : '🌙' }}
        </button>
      </nav>

      <!-- 移动端汉堡按钮 -->
      <button
        class="mobile-menu-btn"
        @click="toggleMobileMenu"
        aria-label="打开菜单"
      >
        <span class="hamburger" :class="{ open: mobileMenuOpen }"></span>
      </button>
    </div>

    <!-- 移动端抽屉菜单 -->
    <Transition name="drawer">
      <div v-if="mobileMenuOpen" class="mobile-drawer">
        <nav class="mobile-nav">
          <a
            v-for="link in navLinks"
            :key="link.link"
            :href="link.link"
            class="mobile-menu-item"
            :class="{ active: isActive(link.link) }"
            @click="closeMobileMenu"
          >
            {{ link.text }}
          </a>
        </nav>
        <div class="mobile-drawer-footer">
          <button
            class="theme-toggle mobile"
            @click="toggleTheme"
          >
            {{ isDark ? '☀️ 浅色模式' : '🌙 深色模式' }}
          </button>
          <div class="mobile-social">
            <a href="https://github.com/Dearchenxiaojie" target="_blank">GitHub</a>
            <a href="mailto:2949536466@qq.com">Email</a>
          </div>
        </div>
      </div>
    </Transition>

    <!-- 遮罩层 -->
    <Transition name="fade">
      <div
        v-if="mobileMenuOpen"
        class="mobile-overlay"
        @click="closeMobileMenu"
      ></div>
    </Transition>
  </header>
</template>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(250, 250, 248, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-light);
  height: var(--nav-height);
}

:root.dark .navbar {
  background: rgba(26, 24, 22, 0.8);
}

.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-6);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--text-primary);
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
  text-decoration: none;
}

.logo-icon {
  font-size: 1.5rem;
}

/* 桌面导航 */
.navbar-menu {
  display: flex;
  align-items: center;
  gap: var(--space-8);
}

.menu-item {
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
  padding: var(--space-2) 0;
  position: relative;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.menu-item:hover {
  color: var(--text-primary);
}

.menu-item.active {
  color: var(--text-primary);
}

.menu-item.active::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--color-primary);
  border-radius: 1px;
}

/* 主题切换按钮 */
.theme-toggle {
  background: none;
  border: none;
  font-size: 1.125rem;
  cursor: pointer;
  padding: var(--space-2);
  border-radius: var(--radius-md);
  line-height: 1;
  transition: background var(--transition-fast);
}

.theme-toggle:hover {
  background: var(--bg-tertiary);
}

.theme-toggle.mobile {
  width: 100%;
  text-align: left;
  font-size: 1rem;
  padding: var(--space-4);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
}

.theme-toggle.mobile:hover {
  background: var(--bg-secondary);
  color: var(--text-primary);
}

/* 移动端汉堡按钮 */
.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  padding: var(--space-2);
  cursor: pointer;
}

.hamburger {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  position: relative;
  transition: background var(--transition-fast);
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  left: 0;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  transition: transform var(--transition-fast);
}

.hamburger::before {
  top: -7px;
}

.hamburger::after {
  bottom: -7px;
}

.hamburger.open {
  background: transparent;
}

.hamburger.open::before {
  transform: translateY(7px) rotate(45deg);
}

.hamburger.open::after {
  transform: translateY(-7px) rotate(-45deg);
}

/* 移动端抽屉菜单 */
.mobile-drawer {
  position: fixed;
  top: var(--nav-height);
  right: 0;
  bottom: 0;
  width: 280px;
  background: var(--bg-page);
  border-left: 1px solid var(--border-light);
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  z-index: 999;
  box-shadow: var(--shadow-xl);
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.mobile-menu-item {
  color: var(--text-secondary);
  font-size: 1.1rem;
  font-weight: 500;
  padding: var(--space-4);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: all var(--transition-fast);
}

.mobile-menu-item:hover {
  background: var(--bg-secondary);
  color: var(--text-primary);
}

.mobile-menu-item.active {
  background: var(--color-primary-50);
  color: var(--color-primary);
}

:root.dark .mobile-menu-item.active {
  background: rgba(196, 149, 106, 0.15);
}

.mobile-drawer-footer {
  margin-top: auto;
  padding-top: var(--space-6);
  border-top: 1px solid var(--border-light);
}

.mobile-social {
  display: flex;
  gap: var(--space-6);
  margin-top: var(--space-4);
}

.mobile-social a {
  color: var(--text-secondary);
  font-size: 0.9rem;
  text-decoration: none;
}

.mobile-social a:hover {
  color: var(--color-primary);
}

/* 遮罩层 */
.mobile-overlay {
  position: fixed;
  top: var(--nav-height);
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 998;
}

/* 动画 */
.drawer-enter-active,
.drawer-leave-active {
  transition: transform var(--transition-slow);
}

.drawer-enter-from,
.drawer-leave-to {
  transform: translateX(100%);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity var(--transition-base);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 响应式 */
@media (max-width: 768px) {
  .navbar-menu {
    display: none;
  }

  .mobile-menu-btn {
    display: block;
  }
}
</style>
