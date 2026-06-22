# 云上日志 v2 改版设计文档

> **项目：** Dearchenxiaojie.github.io（云上日志）
> **日期：** 2026-06-22
> **状态：** 设计稿 v1
> **路线：** 精修升级（不动框架）

---

## 一、背景与目标

### 1.1 现状

「云上日志」是一个基于 VitePress 构建的个人博客站点，部署于 GitHub Pages。整体设计风格温暖文艺（Amber + Stone 色系），按页面场景定制色彩主题（首页暖白、文章页冬日冰蓝、相册页深色展厅、关于页秋日咖啡馆）。

### 1.2 目标

在**不更换框架、不改品牌调性**的前提下，从工程规范、用户体验、设计细节三个维度进行专业升级：

- **工程层面** — 清理仓库、规范化 git 管理、消除构建产物和依赖的提交
- **体验层面** — 暗黑模式、图片性能、无障碍、阅读体验
- **设计层面** — CSS 体系优化、组件状态完善、消除粗糙边缘

### 1.3 不做的事

- ❌ 不迁移到其他框架（不换掉 VitePress）
- ❌ 不改变整体配色体系和品牌调性
- ❌ 不改动文章内容和数据模型

---

## 二、阶段一：工程清洗（P0）

### 2.1 问题清单

| 问题 | 严重程度 | 说明 |
|------|----------|------|
| `node_modules/` 提交到 git | 🔴 | 仓库体积膨胀，clone 慢 |
| `.vitepress/cache/` + `dist/` 提交 | 🔴 | 构建产物不应在版本控制中 |
| 无 `.gitignore` | 🔴 | 缺少基本工程规范 |
| 开发脚本在根目录 | 🟡 | upload-*.py/sh 属于开发工具 |
| 本地 repo 与远程不同步 | 🔴 | 本地有旧版 HTML，远程有新版 VitePress |
| `.superpowers/` 未在 gitignore | 🟡 |  brainstorming 工作目录 |

### 2.2 执行步骤

1. **创建 `.gitignore`**

```
node_modules/
.vitepress/cache/
.vitepress/dist/
.superpowers/
*.py
*.sh
upload-*
```

2. **移除已提交的不需要的文件**

```bash
git rm -r --cached node_modules/
git rm -r --cached .vitepress/cache/
git rm -r --cached .vitepress/dist/
git rm upload-*.py upload-*.sh README-photos.md
```

3. **同步本地仓库**

拉取远程 `main` 分支的最新 VitePress 源码到本地，废弃旧版 HTML。

4. **配置 GitHub Pages 构建**

当前 Pages 从 `main` 分支的 `docs/` 目录构建（已配置）。确认 `Action` 或 `deploy` 脚本可以自动化构建流程。

### 2.3 验收标准

- [ ] `git clone` 速度明显提升
- [ ] `.gitignore` 存在且覆盖所有不应提交的文件类型
- [ ] 本地和远程代码一致，本地可正常 `vitepress dev docs` 预览

---

## 三、阶段二：暗黑模式 + 主题系统（P1）

### 3.1 设计思路

利用现有的 CSS 变量体系扩展深色变量，不新增文件，只在现有 CSS 文件中补充 `:root.dark` 或 `@media (prefers-color-scheme: dark)` 作用域。

### 3.2 色彩映射

| CSS 变量 | 浅色值 | 深色值 |
|----------|--------|--------|
| `--bg-primary` | `#fafaf9` | `#1c1917` |
| `--bg-secondary` | `#f5f5f4` | `#292524` |
| `--bg-card` | `#ffffff` | `#44403c` |
| `--text-primary` | `#1c1917` | `#fafaf9` |
| `--text-secondary` | `#57534e` | `#d6d3d1` |
| `--text-tertiary` | `#78716c` | `#a8a29e` |
| `--border-light` | `#e7e5e4` | `#44403c` |

每页场景色也对应深色版：
- **首页** — 暖白渐变 → 深暖灰渐变
- **文章页（冬·书房）** — `#F5F7FA` → `#0f172a`
- **相册页（夜·展厅）** — 本身已是深色，微调
- **关于页（秋·咖啡馆）** — `#FFF8F0` → `#292524`

### 3.3 切换机制

```typescript
// 优先级：手动切换 > 系统偏好 > 默认浅色
// 手动切换存入 localStorage
// 用 class="dark" 挂载在 <html> 上
```

- 导航栏添加 **🌓 切换按钮**
- 首次访问遵循 `prefers-color-scheme`
- 切换后记住偏好

### 3.4 验收标准

- [ ] 所有页面深色模式视觉完整，无对比度问题
- [ ] 切换按钮可工作，刷新后记住状态
- [ ] 图片在深色模式下显示正常
- [ ] 代码块在深色模式下可读

---

## 四、阶段三：图片体系重构（P1）

### 4.1 问题分析

当前相册架构有四个问题：
1. **原图直出** — 单张照片可达 1-2MB，首页直接加载 5 张全尺寸原图
2. **手动维护** — `photos.json` 需要手动编辑添加新照片路径
3. **缺乏懒加载** — 相册页一次性加载所有图片
4. **布局偏移（CLS）** — 瀑布流用 CSS `columns`，图片加载前无占位

### 4.2 优化方案

**首页相册预览：**
- 取最新 5 张照片，加 `loading="lazy"`
- 每张图包裹在固定宽高比的占位容器中（`aspect-ratio`），消除 CLS
- 图片加 `decoding="async"`

**相册页：**
- 保留现有瀑布流布局
- 加 **Lightbox 灯箱** — 点击照片全屏浏览，左右切换
- 照片懒加载 + 渐进式显示（`@load` 事件 + opacity transition）
- 占位容器设置宽高比

**自动化：**
- 提供一个简单的 Node 脚本扫描 `public/gallery/` 目录，自动生成 `photos.json`
- 在 `package.json` 中添加 `"scripts": { "photos": "node scripts/generate-photos.js" }`

### 4.3 验收标准

- [ ] 首页图片懒加载，未进入视口时不请求
- [ ] 照片加载时无布局跳跃
- [ ] Lightbox 可工作，支持键盘左右切换
- [ ] 相册加载性能有改善（DevTools Network 验证）

---

## 五、阶段四：体验升级（P2）

### 5.1 阅读进度条

文章页顶部固定一个 3px 高的细条，颜色为 `--color-primary`，滚动时根据 `scrollTop / (scrollHeight - clientHeight)` 计算宽度。

- 仅文章页显示
- 不影响现有布局
- 用 `position: fixed; top: 0` 挂载

### 5.2 无障碍（A11y）

| 改进项 | 位置 | 实现方式 |
|--------|------|----------|
| 导航 `aria-label` | 所有导航栏 | `<nav aria-label="主导航">` |
| 焦点可见样式 | 全局 CSS | `:focus-visible` 加 2px 环 |
| 图片 `alt` 文本 | gallery | 从文件名生成有意义的 alt |
| 语义化按钮 | MusicPlayer | 非 div 点击元素改用 `<button>` |

### 5.3 音乐播放器决策

当前 MusicPlayer.vue 是空的占位组件（显示"功能开发中"）。选择其一：

**方案 A：实现基本功能**
- 嵌入一个网易云/QQ 音乐外链 iframe
- 或基于 `<audio>` 标签播放本地音乐文件
- 保留迷你播放器 UI

**方案 B：移除占位**
- 删除 MusicPlayer.vue 及其引用
- 等有真实需求时再实现

**推荐：方案 B（移除占位）**，避免半成品影响印象。

### 5.4 验收标准

- [ ] 文章页阅读进度条显示正常
- [ ] 导航可通过键盘 Tab 遍历，焦点可见
- [ ] 图片有有意义的 alt 文本
- [ ] MusicPlayer 占位已移除（或已实现）

---

## 六、不做但值得关注的事（未来方向）

这些不在本次改版范围内，但值得记录：

- **RSS 订阅** — 增加 `feed.xml` 输出，VitePress 有现成插件
- **访问统计** — 集成 Umami/Plausible 等轻量分析
- **评论系统** — Giscus / Waline 等基于 GitHub Issue 的评论
- **图片 CDN** — 将相册图片迁移到对象存储 + CDN，减小 repo 体积

---

## 七、实施计划

### 依赖关系

```
阶段一（工程清洗） → 阶段二（暗黑模式） → 阶段三（图片优化）
                                               ↓
                                         阶段四（体验升级）
```

阶段一是其他所有阶段的前提（因为需要同步仓库、加 gitignore 之后才能安全修改代码）。

### 预估工作量

| 阶段 | 预估时间 | 涉及文件数 |
|------|----------|-----------|
| 一：工程清洗 | 0.5 天 | 3-5 个（gitignore + 清理） |
| 二：暗黑模式 | 1 天 | 8-10 个（CSS + 组件） |
| 三：图片优化 | 0.5 天 | 5-6 个（组件 + 脚本） |
| 四：体验升级 | 0.5 天 | 4-5 个（组件 + CSS） |
| **合计** | **2.5 天** | **~20 个文件** |
