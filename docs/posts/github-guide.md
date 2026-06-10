---
title: GitHub 入门指南：从注册到使用
date: 2026-06-09
description: 详细介绍 GitHub 的注册、使用方法，以及国内访问加速方案
tags: [GitHub, 工具, 教程]
coverText: "GitHub\n全球最大的代码托管平台"
---

# GitHub 入门指南：从注册到使用

## 什么是 GitHub？

GitHub 是全球最大的代码托管平台，也是开发者社区。你可以在这里：

- 📦 托管自己的代码项目
- 🤝 与其他开发者协作
- 📚 学习优秀的开源项目
- 🚀 部署静态网站（GitHub Pages）

**官网地址**：https://github.com

---

## 注册 GitHub 账号

### 步骤

1. 访问 https://github.com
2. 点击 **Sign up** 按钮
3. 输入邮箱、密码、用户名
4. 完成邮箱验证
5. 选择免费计划（Free）

### 注意事项

- **用户名**：选择一个好记的名字，这会成为你的个人主页地址（如 `github.com/你的用户名`）
- **邮箱**：建议使用常用邮箱，方便接收通知
- **密码**：使用强密码，建议开启两步验证

---

## GitHub 基础概念

### 仓库（Repository）

仓库是项目的基本单位，包含所有的代码文件和历史记录。

- **公开仓库**：所有人可见，适合开源项目
- **私有仓库**：只有你和授权的人可见

### 分支（Branch）

分支用于开发新功能或修复 bug，不影响主分支。

```bash
# 创建新分支
git branch feature-new

# 切换到新分支
git checkout feature-new

# 或者一步完成
git checkout -b feature-new
```

### 提交（Commit）

提交是代码变更的快照，记录了你做了什么修改。

```bash
# 添加文件到暂存区
git add .

# 提交变更
git commit -m "添加了新功能"

# 推送到 GitHub
git push origin main
```

### 拉取请求（Pull Request）

当你想把代码合并到主分支时，需要创建 Pull Request。

---

## 常用 GitHub 功能

### 1. 创建仓库

1. 点击右上角 **+** 号
2. 选择 **New repository**
3. 填写仓库名称和描述
4. 选择公开或私有
5. 点击 **Create repository**

### 2. 上传代码

**方式一：网页上传**
- 在仓库页面点击 **Add file** → **Upload files**
- 拖拽文件到页面
- 点击 **Commit changes**

**方式二：Git 命令行**
```bash
# 克隆仓库
git clone https://github.com/用户名/仓库名.git

# 进入仓库目录
cd 仓库名

# 添加文件
git add .

# 提交
git commit -m "提交信息"

# 推送
git push origin main
```

### 3. GitHub Pages

GitHub Pages 可以免费托管静态网站。

**启用方法：**
1. 进入仓库设置（Settings）
2. 找到 **Pages** 选项
3. 选择分支和目录
4. 点击 **Save**

**访问地址**：`https://用户名.github.io/仓库名`

---

## 国内访问加速

由于网络原因，国内访问 GitHub 可能较慢。以下是几种加速方案：

### 方案一：使用加速器

#### Watt Toolkit（原 Steam++）

Watt Toolkit 是一个免费的多功能工具箱，支持 GitHub 加速。

**下载地址**：https://steampp.net

**使用方法：**
1. 下载并安装 Watt Toolkit
2. 打开软件，找到 **网络加速** 功能
3. 勾选 **GitHub**
4. 点击 **一键加速**

**特点：**
- ✅ 免费开源
- ✅ 支持 Windows/Mac/Linux
- ✅ 不仅加速 GitHub，还支持其他服务
- ✅ 无需注册账号

#### GitHub520

GitHub520 通过修改 hosts 文件加速访问。

**项目地址**：https://github.com/521xueweihan/GitHub520

**使用方法：**
1. 访问项目页面
2. 复制最新的 hosts 内容
3. 粘贴到系统的 hosts 文件中

**hosts 文件位置：**
- Windows：`C:\Windows\System32\drivers\etc\hosts`
- Mac/Linux：`/etc/hosts`

### 方案二：使用镜像站

#### FastGit

**地址**：https://hub.fastgit.xyz

**使用方法：**
- 将 `github.com` 替换为 `hub.fastgit.xyz`
- 例如：`https://hub.fastgit.xyz/用户名/仓库名`

#### GitClone

**地址**：https://gitclone.com

**使用方法：**
- 在仓库地址前加上 `gitclone.com/`
- 例如：`https://gitclone.com/github.com/用户名/仓库名`

### 方案三：修改 Git 配置

```bash
# 使用国内镜像
git config --global url."https://gitclone.com/github.com/".insteadOf "https://github.com/"

# 或者使用 FastGit
git config --global url."https://hub.fastgit.xyz/".insteadOf "https://github.com/"
```

---

## 推荐的 GitHub 项目

### 学习资源

- [free-programming-books](https://github.com/EbookFoundation/free-programming-books) - 免费编程书籍
- [coding-interview-university](https://github.com/jwasham/coding-interview-university) - 编程面试大学
- [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) - 开发者路线图

### 实用工具

- [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) - 终端美化
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k) - Zsh 主题
- [nvm](https://github.com/nvm-sh/nvm) - Node.js 版本管理

### 项目模板

- [VitePress](https://github.com/vuejs/vitepress) - 静态网站生成器
- [Hexo](https://github.com/hexojs/hexo) - 博客框架
- [Vue](https://github.com/vuejs/vue) - 前端框架

---

## 常见问题

### Q: GitHub 免费吗？

A: GitHub 对个人用户免费，包括无限的公开和私有仓库。

### Q: 如何删除仓库？

A: 进入仓库设置（Settings）→ 滚动到底部 → 找到 **Danger Zone** → 点击 **Delete this repository**

### Q: 如何找回密码？

A: 在登录页面点击 **Forgot password**，输入邮箱，按照邮件提示重置密码。

### Q: GitHub 有中文版吗？

A: GitHub 界面主要是英文，但可以通过浏览器翻译功能查看中文。

---

## 总结

GitHub 是开发者必备的工具，无论是学习、协作还是展示项目，都非常有用。希望这篇指南能帮助你快速上手 GitHub！

**记住：**
- 🎯 多看优秀的开源项目
- 📝 养成写 README 的习惯
- 🤝 积极参与开源社区
- 🚀 用 GitHub Pages 展示自己

---

*如果你有任何问题，欢迎在评论区留言！*
