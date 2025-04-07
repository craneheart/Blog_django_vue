import {createRouter, createWebHashHistory} from 'vue-router'
import HomeView from "../views/HomeView.vue"

// 为MPA形式定义路由
// 在MPA中，每个页面都有自己的入口，路由主要用于页面内部导航
const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView,
        meta: {
            title: '首页',
        }
    },
    // 可以添加更多当前页面内部路由
]

// 使用hash模式而不是history模式，避免服务器配置问题
const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes
})

export default router
