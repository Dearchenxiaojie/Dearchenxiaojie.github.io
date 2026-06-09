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
        <span class="player-header-title">♪ 现在播放</span>
        <button class="player-close" @click="toggleExpand">✕</button>
      </div>

      <div class="player-cover">
        <div class="cover-art">🎵</div>
      </div>

      <div class="player-info">
        <p class="song-title">等待播放...</p>
        <p class="song-artist">点击播放按钮开始</p>
      </div>

      <div class="player-progress">
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
        <div class="progress-times">
          <span class="progress-time">0:00</span>
          <span class="progress-time">0:00</span>
        </div>
      </div>

      <div class="player-controls">
        <button class="control-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="19 20 9 12 19 4 19 20"></polygon>
            <line x1="5" y1="19" x2="5" y2="5"></line>
          </svg>
        </button>
        <button class="control-btn play-btn" @click="togglePlay">
          <svg v-if="!isPlaying" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="5 3 19 12 5 21 5 3"></polygon>
          </svg>
          <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="6" y="4" width="4" height="16"></rect>
            <rect x="14" y="4" width="4" height="16"></rect>
          </svg>
        </button>
        <button class="control-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="5 4 15 12 5 20 5 4"></polygon>
            <line x1="19" y1="5" x2="19" y2="19"></line>
          </svg>
        </button>
      </div>

      <div class="player-volume">
        <button class="volume-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
          </svg>
        </button>
        <div class="volume-bar">
          <div class="volume-fill" :style="{ width: (volume * 100) + '%' }"></div>
        </div>
      </div>
    </div>
  </div>
</template>
