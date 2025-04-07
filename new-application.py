import os
import sys


# 模板定义
class VueTemplates:
    APP_VUE = """<template>
  <router-view />
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
  width: 100%;
}

#app {
  height: 100%;
  width: 100%;
}
</style>"""
    MAIN_JS = """import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import api from "@/components/api.vue"
import store from "./store"

import '/src/assets/main.css'

const app = createApp(App)

app.use(router)
app.use(store)
app.mount('#app')
app.component("api", api)"""
    INDEX_HTML = """<!DOCTYPE html>
<html lang="">
<head>
    <meta charset="UTF-8">
    <link href="/favicon.ico" rel="icon">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>Vite App</title>
</head>
<body>
<div id="app"></div>
<script src="./main.js" type="module"></script>
</body>
</html>"""
    ROUTER_INDEX_JS = """import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from "../views/HomeView.vue"

// 为MPA形式定义路由
// 在MPA中，每个页面都有自己的入口，路由主要用于页面内部导航
const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView,
        meta:{
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

export default router"""
    STORE_INDEX_JS = """import {createStore} from 'vuex'
export default createStore(
    {
        state: {},
        getters: {},
        mutations: {},
        actions: {},
        modules: {}
    }
)"""
    HOME_VIEW = """<script setup>

</script>

<template>

</template>

<style scoped>

</style>"""


# Django应用模板
DJANGO_APPLICATION_TEMPLATE = {
    "dir": ["migrations", "models", "views"],
    "file": {
        "": {
            "__init__.py": "",
            "admin.py": "from django.contrib import admin\n\n# Register your models here.",
            "apps.py": "from django.apps import AppConfig\n\n\nclass {{app_name}}Config(AppConfig):\n    default_auto_field = 'django.db.models.BigAutoField'\n    name = '{{app_name}}'",
            "urls.py": "from django.urls import path, include, re_path\nfrom .views import api\nfrom vue.vue import Index\n\nurlpatterns = [\n    re_path(r'^(?!api/).*$', Index.get(\"{{app_name}}\")),\n    path(\"api/\", include(api)),\n]",
        },
        "migrations": {
            "__init__.py": "",
        },
        "models": {
            "__init__.py": "",
            "models.py": "from django.db import models\n\n# Create your models here.",
        },
        "views": {
            "__init__.py": "",
            "api.py": "from django.urls import path\n\nurlpatterns = []",
        },
    },
}

# Vue应用模板
VUE_APPLICATION_TEMPLATE = {
    "dir": ["components", "router", "store", "views"],
    "file": {
        "": {
            "App.vue": VueTemplates.APP_VUE,
            "main.js": VueTemplates.MAIN_JS,
            "index.html": VueTemplates.INDEX_HTML,
        },
        "router": {
            "index.js": VueTemplates.ROUTER_INDEX_JS,
        },
        "store": {
            "index.js": VueTemplates.STORE_INDEX_JS,
        },
        "views": {
            "HomeView.vue": VueTemplates.HOME_VIEW,
        },
    }
}


def template_maker(root_dir: str, template: dict, application_name: str) -> bool:
    """
    根据提供的模板在指定目录创建应用结构
    
    Args:
        root_dir: 应用根目录路径
        template: 应用模板字典
        application_name: 应用名称
        
    Returns:
        bool: 创建是否成功
    """
    try:
        # 创建所有目录
        for dir_name in template["dir"]:
            dir_path = os.path.join(root_dir, dir_name)
            if not check_and_create_path(dir_path):
                print(f"警告: 目录 {dir_path} 已存在，将继续使用现有目录")

        # 创建所有文件
        for dir_path, files in template["file"].items():
            current_dir = os.path.join(root_dir, dir_path)
            os.makedirs(current_dir, exist_ok=True)

            for file_name, content in files.items():
                # 替换模板中的应用名称
                content = content.replace("{{app_name}}", application_name)
                file_path = os.path.join(current_dir, file_name)
                if not create_file(file_path, content):
                    print(f"错误: 文件 {file_path} 创建失败")
                    return False
        return True
    except Exception as e:
        print(f"错误: 创建模板时出现异常: {e}")
        return False


def check_and_create_path(dir_path: str) -> bool:
    """
    检查并创建目录路径
    
    Args:
        dir_path: 要创建的目录路径
        
    Returns:
        bool: True表示创建了新目录，False表示目录已存在
    """
    if os.path.exists(dir_path):
        return False
    else:
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"错误: 创建目录 {dir_path} 时出错: {e}")
            sys.exit(1)


def create_file(file_path: str, content="") -> bool:
    """
    创建并写入文件
    
    Args:
        file_path: 文件路径
        content: 文件内容
        
    Returns:
        bool: 操作是否成功
    """
    try:
        # 检查文件是否已存在
        if os.path.exists(file_path):
            print(f"警告: 文件 {file_path} 已存在，将被覆盖")

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"创建文件: {file_path}")
        return True
    except Exception as e:
        print(f"错误: 创建文件 {file_path} 时出错: {e}")
        return False


def create_application(application_name: str) -> bool:
    """
    创建Django和Vue应用
    
    Args:
        application_name: 应用名称
        
    Returns:
        bool: 创建是否成功
    """
    print(f"开始创建应用 '{application_name}'...")

    # 设置应用目录路径
    django_app_dir = os.path.join("backend", application_name)

    # 检查并创建应用目录
    if not check_and_create_path(django_app_dir):
        print(f"警告: Django应用目录 {django_app_dir} 已存在，可能会覆盖现有文件")

    # 使用template_maker创建Django应用结构
    if not template_maker(django_app_dir, DJANGO_APPLICATION_TEMPLATE, application_name):
        print(f"错误: Django应用 '{application_name}' 创建失败")
        return False

    # 创建 Vue 应用目录
    vue_app_dir = os.path.join("frontend", "src", "pages", application_name)

    # 检查并创建Vue应用目录
    if not check_and_create_path(vue_app_dir):
        print(f"警告: Vue应用目录 {vue_app_dir} 已存在，可能会覆盖现有文件")

    # 使用template_maker创建Vue应用结构
    if not template_maker(vue_app_dir, VUE_APPLICATION_TEMPLATE, application_name):
        print(f"错误: Vue应用 '{application_name}' 创建失败")
        return False

    print(f"应用 '{application_name}' 创建成功!")
    print(f"Django应用路径: {os.path.abspath(django_app_dir)}")
    print(f"Vue应用路径: {os.path.abspath(vue_app_dir)}")
    return True


def is_valid_application_name(name):
    """
    验证应用名称是否有效
    
    Args:
        name: 待验证的应用名称
        
    Returns:
        tuple: (是否有效, 错误消息)
    """
    # 检查应用名称是否包含非法字符
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', ' ', '-']
    django_reserved_names = ['django', 'test', 'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles']

    # 检查是否为空或只包含空格
    if not name or name.isspace():
        return False, "应用名称不能为空"

    # 检查开头和结尾是否有空格
    if name != name.strip():
        return False, "应用名称不能以空格开头或结尾"

    # 检查非法字符
    for char in invalid_chars:
        if char in name:
            return False, f"应用名称不能包含非法字符: '{char}'"

    # 检查是否以数字开头
    if name[0].isdigit():
        return False, "应用名称不能以数字开头"

    # 检查是否以点结尾（Windows系统限制）
    if name.endswith('.'):
        return False, "应用名称不能以点(.)结尾"

    # 检查是否是Django保留名称
    if name.lower() in django_reserved_names:
        return False, f"'{name}'是Django的保留名称，请使用其他名称"

    return True, ""


def main():
    """主函数，处理用户输入并创建应用"""
    print("=== Django-Vue应用创建工具 ===")

    while True:
        application_name = input("\n请输入应用名称 (输入'q'退出): ").strip()

        if application_name.lower() == 'q':
            print("退出应用创建")
            break

        valid, error_msg = is_valid_application_name(application_name)

        if valid:
            confirm = input(f"将创建应用 '{application_name}'，确认? (y/n): ").strip().lower()
            if confirm == 'y':
                if create_application(application_name):
                    again = input("\n是否继续创建其他应用? (y/n): ").strip().lower()
                    if again != 'y':
                        break
            else:
                print("已取消创建")
        else:
            print(f"错误: {error_msg}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程序被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"程序运行出错: {e}")
        sys.exit(1)
