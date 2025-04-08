import { ref, onMounted, watch } from 'vue'

export function useTheme() {
  const isDark = ref(false)

  // 切换主题
  const toggleTheme = () => {
    isDark.value = !isDark.value
    updateTheme()
  }

  // 更新DOM和本地存储
  const updateTheme = () => {
    // 更新DOM
    if (isDark.value) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }

    // 保存到localStorage
    localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
  }

  // 初始化主题
  onMounted(() => {
    // 优先从localStorage读取主题设置
    const savedTheme = localStorage.getItem('theme')

    if (savedTheme === 'dark') {
      isDark.value = true
    } else if (savedTheme === 'light') {
      isDark.value = false
    } else {
      // 如果没有保存的主题设置，则根据系统偏好设置
      isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches
    }

    updateTheme()
  })

  return {
    isDark,
    toggleTheme
  }
}

//使用
// <template>
//   <div>
//     <button @click="toggleTheme" class="theme-toggle">
//       {{ isDark ? '切换到浅色模式' : '切换到深色模式' }}
//     </button>
//     <!-- 其他应用内容 -->
//   </div>
// </template>
//
// <script setup>
// import { useTheme } from '@/components/useTheme'
//
// const { isDark, toggleTheme } = useTheme()
// </script>