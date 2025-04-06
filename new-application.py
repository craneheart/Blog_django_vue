import os

DJANGO_APPLICATION_TEMPLATE = {
    "dir": ["migrations", "models", "views"],
    "file": {
        "": {
            "__init__.py": "",
            "admin.py": "from django.contrib import admin\n\n# Register your models here.",
            "apps.py": "from django.apps import AppConfig\n\n\nclass {{app_name}}Config(AppConfig):\n    default_auto_field = 'django.db.models.BigAutoField'\n    name = '{{app_name}}'",
            "urls.py": "from django.urls import path\n\nurlpatterns = []",
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

VUE_APPLICATION_TEMPLATE = {
    "dir": ["components", "router", "store", "views"],
    "file": {
        "": {
            "App.vue": "<template>\n</template>\n<script>\n</script>",
            "main.js": "import { createApp } from 'vue'\nimport App from './App.vue'\n\ncreateApp(App).mount('#app')",
            "":""
            # TODO:先写出一个简单的vue模板.
        }
    }
}

def template_maker(root_dir:str, template:dict, application_name:str) -> bool:
    for dir_name in template["dir"]:
        dir_path = os.path.join(root_dir, dir_name)
        if not check_and_create_path(dir_path):
            print(f"{root_dir}中,目录{dir_path}已经存在")
            return False

    for dir_path, files in template["file"].items():
        current_dir = os.path.join(root_dir, dir_path)
        for file_name, content in files.items():
            # 替换模板中的应用名称
            content = content.replace("{{app_name}}", application_name)
            file_path = os.path.join(current_dir, file_name)
            if not create_file(file_path, content):
                print(f"文件{file_path}创建失败")
                return False
    return True

def check_and_create_path(dir_path):
    if os.path.exists(dir_path):
        print("应用已存在:")
        return False
    else:
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"创建路径时出错: {e}")
            return False


def create_file(file_path, content=""):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"创建文件: {file_path}")
        return True
    except Exception as e:
        print(f"创建文件时出错: {e}")
        return False


def creat_application(application_name):
    # 设置应用目录路径
    django_app_dir = os.path.join("backend", application_name)

    # 检查并创建应用目录
    if not check_and_create_path(django_app_dir):
        print("django应用已经存在")
        return False

    # 创建子目录
    for dir_name in DJANGO_APPLICATION_TEMPLATE["dir"]:
        dir_path = os.path.join(django_app_dir, dir_name)
        if not check_and_create_path(dir_path):
            print("django应用,子目录已经存在")
            return False

    # 创建文件
    for dir_path, files in DJANGO_APPLICATION_TEMPLATE["file"].items():
        current_dir = os.path.join(django_app_dir, dir_path)
        for file_name, content in files.items():
            # 替换模板中的应用名称
            content = content.replace("{{app_name}}", application_name)
            file_path = os.path.join(current_dir, file_name)
            if not create_file(file_path, content):
                print("django应用创建失败")
                return False

    print(f"应用 '{application_name}' 创建成功!")

    # 创建 Vue 应用目录
    vue_app_dir = os.path.join("frontend", "src", "pages", application_name)
    return True


def main():
    application_name = input("请输入应用名称: ")
    if application_name.strip():
        creat_application(application_name)
    else:
        print("应用名称不能为空")


if __name__ == "__main__":
    main()
