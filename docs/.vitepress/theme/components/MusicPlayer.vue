<script setup>
import { ref, onMounted } from 'vue'

const isPlaying = ref(false)
const isExpanded = ref(false)
const volume = ref(0.3)
const currentSong = ref('')
const progress = ref(0)

const togglePlay = () => {
  isPlaying.value = !isPlaying.value
}

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <div class="music-player" :class="{ expanded: isExpanded }">
    <!-- 收起状态 -->
    <div class="player-mini" @click="toggleExpand">
      <div class="player-icon" :class="{ spinning: isPlaying }">
        ♪
      </div>
    </div>

    <!-- 展开状态 -->
    <div v-if="isExpanded" class="player-expanded">
      <div class="player-header">
        <span>♪ 现在播放</span>
        <button class="close-btn" @click="toggleExpand">✕</button>
      </div>

      <div class="player-cover">
        <div class="cover-art">🎵</div>
      </div>

      <div class="player-info">
        <p class="song-name">等待播放...</p>
        <p class="song-artist">点击播放按钮开始</p>
      </div>

      <div class="player-progress">
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
        <div class="progress-time">
          <span>0:00</span>
          <span>0:00</span>
        </div>
      </div>

      <div class="player-controls">
        <button class="ctrl-btn">⏮</button>
        <button class="ctrl-btn play-btn" @click="togglePlay">
          {{ isPlaying ? '⏸' : '▶' }}
        </button>
        <button class="ctrl-btn">⏭</button>
      </div>
    </div>
  </div>
</template>
