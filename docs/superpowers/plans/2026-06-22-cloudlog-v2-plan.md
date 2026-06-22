# 云上日志 v2 改版 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 对 Dearchenxiaojie.github.io（云上日志）进行工程清洗、暗黑模式、图片优化、体验升级四阶段改版

**Architecture:** 在现有 VitePress 项目上做增量修改，不迁移框架。改版集中在 `.vitepress/theme/` 下的 Vue 组件和 CSS 文件，辅以仓库根目录的工程配置调整。

**Tech Stack:** VitePress 1.6.4 + Vue 3.5.35 + 纯 CSS 变量体系（无预处理器）

---

## 文件变更总览

### 创建
- `.gitignore`
- `scripts/generate-photos.js`

### 修改
- `.vitepress/theme/styles/global.css` — 暗黑变量 + focus 样式
- `.vitepress/theme/styles/home.css` — 暗黑适配
- `.vitepress/theme/styles/posts.css` — 暗黑适配
- `.vitepress/theme/styles/gallery.css` — 暗黑适配 + Lightbox
- `.vitepress/theme/styles/about.css` — 暗黑适配
- `.vitepress/theme/Layout.vue` — 暗黑初始化 + 阅读进度条
- `.vitepress/theme/components/HomeLayout.vue` — 暗黑按钮 + 图片懒加载
- `.vitepress/theme/components/GalleryLayout.vue` — 暗黑按钮 + Lightbox
- `.vitepress/theme/components/AboutLayout.vue` — 暗黑按钮
- `.vitepress/theme/components/ToolsLayout.vue` — 暗黑按钮
- `.vitepress/theme/components/SavesLayout.vue` — 暗黑按钮
- `.vitepress/theme/components/MusicPlayer.vue` — 移除

### 删除（git rm --cached）
- `node_modules/`
- `.vitepress/cache/`
- `.vitepress/dist/`
- `upload-*.py`、`upload-*.sh`、`README-photos.md`

---

## 阶段一：工程清洗

### Task 1.1：创建 .gitignore

**文件：** 创建 `.gitignore`

- [ ] **创建 .gitignore**

```gitignore
# 依赖
node_modules/

# 构建产物
.vitepress/cache/
.vitepress/dist/

# 开发脚本
*.py
*.sh
upload-*

# 编辑器
.vscode/
.idea/

# 操作系统
.DS_Store
Thumbs.db

# brainstorming 工作目录
.superpowers/
```

- [ ] **提交**

```bash
git add .gitignore
git commit -m "chore: add .gitignore"
```

### Task 1.2：清理仓库

- [ ] **从 git 跟踪中移除不需要的文件**

```bash
git rm -r --cached node_modules/
git rm -r --cached .vitepress/cache/
git rm -r --cached .vitepress/dist/
git rm upload-imgse.py upload-photos.py upload-photos.sh upload-to-imgur.py README-photos.md
```

- [ ] **提交**

```bash
git commit -m "chore: remove build artifacts and dev scripts from git tracking"
```

### Task 1.3：同步本地仓库

- [ ] **拉取远程 main 分支，废弃本地旧版 HTML**

```bash
git fetch origin main
git stash  # 保存本地未提交修改
git reset --hard origin/main
```

---

## 阶段二：暗黑模式

### Task 2.1：global.css 添加暗黑变量

**文件：** 修改 `docs/.vitepress/theme/styles/global.css`

- [ ] **在文件末尾添加 dark 模式变量集**

```css
:root.dark {
  --color-primary-50: #451a03;
  --color-primary-100: #78350f;
  --color-primary-200: #92400e;
  --color-primary-300: #b45309;
  --color-primary-400: #d97706;
  --color-primary-500: #f59e0b;
  --color-primary-600: #fbbf24;
  --color-primary-700: #fcd34d;
  --color-primary-800: #fde68a;
  --color-primary-900: #fef3c7;
  --color-primary-950: #fffbeb;

  --bg-primary: #1c1917;
  --bg-secondary: #292524;
  --bg-tertiary: #44403c;
  --bg-card: #292524;
  --bg-code: #0c0a09;

  --text-primary: #fafaf9;
  --text-secondary: #d6d3d1;
  --text-tertiary: #a8a29e;
  --text-inverse: #1c1917;
  --text-link: #fbbf24;

  --border-light: #44403c;
  --border-default: #57534e;
  --border-dark: #78716c;

  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.4);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.5);

  --color-stone-50: #1c1917;
  --color-stone-100: #292524;
  --color-stone-200: #44403c;
  --color-stone-300: #57534e;
  --color-stone-400: #78716c;
  --color-stone-500: #a8a29e;
  --color-stone-600: #d6d3d1;
  --color-stone-700: #e7e5e4;
  --color-stone-800: #f5f5f4;
  --color-stone-900: #fafaf9;
  --color-stone-950: #fafaf9;
}
```

### Task 2.2：Layout.vue 添加暗黑初始化和阅读进度条

**文件：** 修改 `docs/.vitepress/theme/Layout.vue`

- [ ] **在 `<script setup>` 添加暗黑模式和进度条逻辑**

```vue
<script setup>
import { ref, onMounted, onUnmounted } from "vue"
// 现有导入保持不变 ...

// 暗黑模式
function initTheme() {
  const saved = localStorage.getItem("cloudlog-theme")
  if (saved === "dark") {
    document.documentElement.classList.add("dark")
  } else if (saved === "light") {
    document.documentElement.classList.remove("dark")
  } else {
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches
    if (prefersDark) document.documentElement.classList.add("dark")
  }
}

// 阅读进度条
const readingProgress = ref(0)
function updateProgress() {
  const scrollTop = window.scrollY
  const docHeight = document.documentElement.scrollHeight - window.innerHeight
  readingProgress.value = docHeight > 0 ? Math.min(scrollTop / docHeight, 1) : 0
}

onMounted(() => {
  initTheme()
  window.addEventListener("scroll", updateProgress)
})

onUnmounted(() => {
  window.removeEventListener("scroll", updateProgress)
})
</script>
```

- [ ] **在模板中添加阅读进度条（在 `<div class="cloudlog-app">` 内部最前面）**

```html
<div v-if="pageStyle === 'posts'" class="reading-progress"
     :style="{ width: readingProgress * 100 + '%' }"></div>
```

- [ ] **添加样式**

```css
.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--color-primary-500);
  z-index: 10000;
  transition: width 0.1s linear;
  border-radius: 0 2px 2px 0;
}
```

### Task 2.3：给所有导航栏添加暗黑切换按钮

**文件：** `HomeLayout.vue`, `GalleryLayout.vue`, `AboutLayout.vue`, `ToolsLayout.vue`, `SavesLayout.vue`

- [ ] **在每个导航栏的菜单项后面加上切换按钮**

```html
<button
  class="theme-toggle"
  onclick="document.documentElement.classList.toggle('dark');localStorage.setItem('cloudlog-theme',document.documentElement.classList.contains('dark')?'dark':'light')"
  aria-label="切换暗黑模式"
>🌓</button>
```

- [ ] **在每个组件的 `<style>` 中添加按钮样式**

```css
.theme-toggle {
  background: none; border: none;
  font-size: 1.125rem; cursor: pointer;
  padding: 0.25rem; border-radius: var(--radius-md);
  line-height: 1; margin-left: 0.5rem;
}
.theme-toggle:hover { background: var(--bg-tertiary); }
```

### Task 2.4：场景页深色背景适配

**文件：** `Layout.vue` 的 `<style scoped>`

- [ ] **为每个场景添加 dark 变体**

```css
:root.dark .scene-home {
  background: linear-gradient(135deg, #292524 0%, #1c1917 33%, #292524 66%, #1c1917 100%);
}
:root.dark .scene-posts { background: #0f172a; }
:root.dark .scene-about {
  background: linear-gradient(135deg, #292524 0%, #44403c 50%, #292524 100%);
}
```

---

## 阶段三：图片优化

### Task 3.1：创建 photos.json 自动生成脚本

**文件：** 创建 `scripts/generate-photos.js`

- [ ] **编写脚本**

```javascript
const fs = require("fs")
const path = require("path")
const galleryDir = path.join(__dirname, "..", "docs", "public", "gallery")
const outputFile = path.join(__dirname, "..", "docs", ".vitepress", "theme", "photos.json")

function scan(dir) {
  const result = {}
  const years = fs.readdirSync(dir).filter(f => /^\d{4}$/.test(f)).sort()
  for (const year of years) {
    const yearDir = path.join(dir, year)
    const months = fs.readdirSync(yearDir).filter(f => /^\d{2}$/.test(f)).sort()
    result[year] = {}
    for (const month of months) {
      result[year][month] = fs.readdirSync(path.join(yearDir, month))
        .filter(f => /\.(jpg|jpeg|png|webp)$/i.test(f)).sort()
    }
  }
  return result
}

fs.writeFileSync(outputFile, JSON.stringify(scan(galleryDir), null, 2), "utf-8")
console.log("photos.json generated")
```

- [ ] **运行脚本**

```bash
node scripts/generate-photos.js
```

### Task 3.2：首页相册预览懒加载

**文件：** 修改 `docs/.vitepress/theme/components/HomeLayout.vue`

- [ ] **将相册图片改为懒加载 + 占位容器**

```html
<div class="gallery-item" style="aspect-ratio:4/3;overflow:hidden;border-radius:var(--radius-lg);background:var(--bg-tertiary)">
  <img :src="photo.src" :alt="photo.alt" loading="lazy" decoding="async"
       style="width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 0.3s"
       @load="$el.style.opacity=1" />
</div>
```

### Task 3.3：相册页添加 Lightbox

**文件：** 修改 `docs/.vitepress/theme/components/GalleryLayout.vue`

- [ ] **添加 Lightbox 状态和函数**

```vue
<script setup>
// 在现有 script 中添加
import { ref, computed, onMounted, onUnmounted } from "vue"

const lbOpen = ref(false)
const lbIndex = ref(0)

const allPhotos = computed(() => {
  const list = []
  months.value.forEach(m => m.photos.forEach(p => list.push(p)))
  return list
})

function openLB(i) { lbIndex.value = i; lbOpen.value = true }
function closeLB() { lbOpen.value = false }
function prevLB() { if (lbIndex.value > 0) lbIndex.value-- }
function nextLB() { if (lbIndex.value < allPhotos.value.length - 1) lbIndex.value++ }
function onKey(e) {
  if (!lbOpen.value) return
  if (e.key === "Escape") closeLB()
  if (e.key === "ArrowLeft") prevLB()
  if (e.key === "ArrowRight") nextLB()
}
onMounted(() => window.addEventListener("keydown", onKey))
onUnmounted(() => window.removeEventListener("keydown", onKey))
</script>
```

- [ ] **在模板底部添加 Lightbox**

```html
<Teleport to="body">
  <div v-if="lbOpen" class="lightbox-overlay" @click.self="closeLB">
    <button class="lightbox-close" @click="closeLB">✕</button>
    <button v-if="lbIndex>0" class="lightbox-nav lightbox-prev" @click="prevLB">‹</button>
    <div class="lightbox-content">
      <img :src="allPhotos[lbIndex].src" :alt="allPhotos[lbIndex].name" class="lightbox-image" />
      <p class="lightbox-caption">{{ allPhotos[lbIndex].name }}</p>
    </div>
    <button v-if="lbIndex<allPhotos.length-1" class="lightbox-nav lightbox-next" @click="nextLB">›</button>
  </div>
</Teleport>
```

### Task 3.4：Lightbox 样式

**文件：** 修改 `docs/.vitepress/theme/styles/gallery.css`

- [ ] **添加 Lightbox CSS**

```css
.lightbox-overlay {
  position:fixed; inset:0; z-index:9999;
  background:rgba(0,0,0,0.9);
  display:flex; align-items:center; justify-content:center;
}
.lightbox-close {
  position:absolute; top:1.5rem; right:1.5rem;
  width:2.5rem; height:2.5rem; border-radius:50%;
  background:rgba(255,255,255,0.1); color:#fff;
  font-size:1.25rem; border:none; cursor:pointer; z-index:1;
}
.lightbox-nav {
  position:absolute; top:50%; transform:translateY(-50%);
  width:3rem; height:3rem; border-radius:50%;
  background:rgba(255,255,255,0.1); color:#fff;
  font-size:2rem; border:none; cursor:pointer; z-index:1;
}
.lightbox-prev { left:1.5rem; }
.lightbox-next { right:1.5rem; }
.lightbox-content { max-width:90vw; max-height:85vh; text-align:center; }
.lightbox-image { max-width:100%; max-height:80vh; object-fit:contain; border-radius:0.5rem; }
.lightbox-caption { color:rgba(255,255,255,0.7); font-size:0.875rem; margin-top:0.75rem; }
```

---

## 阶段四：体验升级

### Task 4.1：移除 MusicPlayer 占位组件

**文件：** 修改 `docs/.vitepress/theme/components/MusicPlayer.vue` + `docs/.vitepress/theme/Layout.vue`

- [ ] **将 MusicPlayer.vue 清空**

```vue
<template></template>
```

- [ ] **从 Layout.vue 删除 MusicPlayer 的 import 和模板引用**

删除 `import MusicPlayer from './components/MusicPlayer.vue'` 和 `<MusicPlayer />` 模板标签。

### Task 4.2：全局无障碍改进

**文件：** 修改 `docs/.vitepress/theme/styles/global.css` + 各 Layout 组件

- [ ] **在 global.css 添加 focus-visible 样式**

```css
:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
button:focus:not(:focus-visible),
a:focus:not(:focus-visible) { outline: none; }
```

- [ ] **给所有导航 `<nav>` 加 aria-label**

在每个 Layout 组件的 `<nav>` 标签上添加 `aria-label="主导航"`。

---

## 验证方式

每个阶段完成后运行：

```bash
cd D:\my-projects\Dearchenxiaojie.github.io
npx vitepress dev docs
```

然后在浏览器中打开 `http://localhost:5173` 预览验证。
