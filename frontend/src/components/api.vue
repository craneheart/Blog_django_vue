<script setup>
import { onMounted } from "vue";

// 请全部使用相对路由, 以此来保证调试可迁移性
async function get(url){
  try{
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  }catch (error){
    console.log("API错误",error);
    throw error;
  }
}

async function post(url, data){
  try{
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken() // 添加CSRF令牌
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  }catch (error){
    console.log("API错误",error);
    throw error;
  }
}

function getCsrfToken() {
  const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];
  console.log(cookieValue)
  //TODO: 验证函数功能,设置后端初始化CSRF的cookie路由
  return cookieValue || '';
}

onMounted(()=>{
  //TODO:检查CSRF口令
})
</script>

<template>

</template>

<style scoped>

</style>