import asyncio
import os
import json

APPLICATION_LIST = [
    "Documents",
    "Index",
]
NPM_PATH = "/home/crane/.config/JetBrains/PyCharm2024.3/node/versions/20.15.0/bin/npm"
NODE_DIR = os.path.dirname(NPM_PATH)


async def npm_build():
    env = os.environ.copy()
    env["PATH"] = f"{NODE_DIR}:{env.get('PATH', '')}"
    process = await asyncio.create_subprocess_shell(
        cmd=f'{NPM_PATH} run build',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd="frontend",
        env=env,
    )
    stdout, stderr = await process.communicate()
    print(stdout.decode())


def static_files():
    # 获取后端静态目录路径
    backend_static_path = os.path.join("backend", "static")
    # 获取前端构建后的静态目录路径
    frontend_static_path = os.path.join("frontend", "dist", "static")

    # 检查后端静态目录是否存在，如果存在则删除
    if os.path.exists(backend_static_path):
        import shutil
        shutil.rmtree(backend_static_path)
        print(f"已删除目录: {backend_static_path}")

    # 将前端构建的静态目录复制到后端
    import shutil
    shutil.copytree(frontend_static_path, backend_static_path)
    print(f"已将 {frontend_static_path} 复制到 {backend_static_path}")


def set_application(app_name):
    app_path = os.path.join("backend", "vue", app_name)
    if not os.path.exists(app_path):
        os.makedirs(app_path)
        print(f"已创建目录: {app_path}")
    index_path = os.path.join(app_path, "index.html")
    if os.path.exists(index_path):
        os.remove(index_path)
        print(f"已删除文件: {index_path}")
    source_path = os.path.join("frontend", "dist", "src", "pages", app_name, "index.html")
    with open(source_path, "r") as source_file:
        source_content = source_file.read()
    with open(index_path, "w") as target_file:
        target_file.write(source_content)
    print(f"已将 {source_path} 复制到 {index_path}")


def set_application_json():
    with open(os.path.join("backend", "vue", "application.json"), "w", encoding="utf-8") as source_file:
        json.dump(APPLICATION_LIST, source_file, ensure_ascii=False, indent=4)


async def main():
    await npm_build()
    static_files()  # 调用静态文件处理函数
    for app_name in APPLICATION_LIST:
        set_application(app_name)
    set_application_json()


if __name__ == "__main__":
    print(asyncio.run(main()))
