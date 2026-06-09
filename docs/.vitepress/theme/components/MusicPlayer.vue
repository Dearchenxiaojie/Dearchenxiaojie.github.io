<script setup>
import { ref, onMounted } from 'vue'

const isPlaying = ref(false)
const isExpanded = ref(false)
const volume = ref(0.3)
const progress = ref(0)

const togglePlay = () => {
  isPlaying.value = !isPlaying.value
}

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <div class="music-player">
    <!-- 迷你播放器 -->
    <div class="player-mini" :class="{ playing: isPlaying }" @click="toggleExpand">
      <div class="player-icon" :class="{ spinning: isPlaying }">
        ♪
      </div>
    </div>

    <!-- 展开播放器 -->
    <div v-if="isExpanded" class="player-expanded">
      <div class="player-header">
        <span class="player-header-title">♪ 音乐播放器</span>
        <button class="player-close" @click="toggleExpand">✕</button>
      </div>

      <div class="player-dev-notice">
        <div class="dev-icon">🚧</div>
        <h4>功能开发中</h4>
        <p>音乐播放器正在开发中，敬请期待！</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* 开发中提示 */
.player-dev-notice {
  padding: 2rem;
  text-align: center;
}

.dev-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.player-dev-notice h4 {
  font-family: var(--font-serif);
  font-size: 1.125rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.player-dev-notice p {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin: 0;
}
</style>
