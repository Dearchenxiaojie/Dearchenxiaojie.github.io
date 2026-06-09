---
title: 文章列表
layout: page
---

<script setup>
import { data as posts } from '../.vitepress/theme/posts.data.mjs'
</script>

# 📝 文章列表

<div class="posts-list">
  <a v-for="post in posts" :key="post.url" :href="post.url" class="post-item">
    <div class="post-date">{{ post.date }}</div>
    <div class="post-content">
      <h3>{{ post.title }}</h3>
      <p>{{ post.description }}</p>
      <div class="post-tags">
        <span v-for="tag in post.tags" :key="tag" class="tag">#{{ tag }}</span>
      </div>
    </div>
  </a>
</div>

<style>
.posts-list {
  margin-top: 2rem;
}

.post-item {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem;
  margin-bottom: 1rem;
  background: rgba(255, 248, 240, 0.5);
  border-radius: 16px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  border: 1px solid rgba(240, 230, 216, 0.5);
}

.post-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(139, 115, 85, 0.1);
}

.post-date {
  font-size: 14px;
  color: #C4956A;
  font-weight: 600;
  min-width: 80px;
  padding-top: 0.2rem;
}

.post-content h3 {
  font-size: 18px;
  margin-bottom: 0.5rem;
  color: #3D3229;
}

.post-content p {
  font-size: 14px;
  color: #8B7355;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

.post-tags {
  display: flex;
  gap: 0.5rem;
}

.tag {
  font-size: 12px;
  color: #C4956A;
  background: rgba(196, 149, 106, 0.1);
  padding: 2px 8px;
  border-radius: 20px;
}
</style>
