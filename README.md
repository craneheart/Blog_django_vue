# Blog_django_vue

简体中文 | [English](./README_en.md)

---

## 简介

使用Django作为后端, vue作为前端框架的一种MPA解决方案,

### 亮点

- 给出vue3使用MPA的模板方案
- 提供一种Django使用vue3的MPA方案的标准路由格式(思路), 以及前端Application
- 使用python自动化脚本, 自动编译, 替换Application的静态文件.

## 模板结构讲解

### Django

在项目的根目录下面, 有如下结构

```
--backend
  |--> application 1
  |--> application 2
  ... ...
  |--> static # 放置静态文件
  |--> vue    # 引用vue application
  |--> manage.py
```

- 其中static是存放静态文件的, 在vue中编译出的的静态文件,如js,css等存放于此
- vue是使用其他Django使用vue application的入口

#### Django中的vue模板入口

vue目录结构如下

```
--vue
  |--> default
  |--> vue application 1
    |--> index.html
  |--> vue application 2
    |--> index.html
  ... ...
  |--> application.json
  |--> vue.py

```

- `default` : 存放默认页面的页面,如vue.py未找到该应用,返回的页面
- `index.html` : vue application入口 index.html
- `application.json` : 运行`pkg-frontend.py`自动生成的 vue application 注册json
- `vue` : 主要的包, 作用是简化index.html的路由注册

### Vue3

页面的设置在`vite.config.js`中
然后页面的结构src如下

```
--src
  |--> assets
  |--> components # 公共组件
  |--> pages
    |--> application 1 #其中一个多页面应用
      |--> conponents
      |--> router
        |--> index.js
      |--> store
        |--> index.js
      |--> views
        |--> example.vue
      |--> App.vue
      |--> index.html
      |--> main.js
```

## 使用

新建一个vue+django application

### 手动创建

#### 创建vue application

根据上面vue3的结构, 新建一个vue application, 其中的index.html, main.js, router/index.js, store/index.js,
App.vue等文件需要自己创建

#### 创建django application

在django的根目录下, 新建一个application, 其中的urls.py, views(python软件包)等文件需要自己创建

然后开始设置django应用

1. 在`settings.py`中, 添加应用
2. 在`backend/urls.py`中, 添加应用的路由
3. 在`你的application路径/urls.py`中, 启用下面设置

```python
from django.urls import path, include, re_path
from .views import api
from vue.vue import Index

urlpatterns = [
    re_path(r'^(?!api/).*$', Index.get("你的application名")),
    path("api/", include(api)),
]
```

4. 在`你的application名/views.py`中, 启用下面设置

创建一个api.py, 路由这样

```python
from django.urls import path

urlpatterns = [

]
```

- 这样,实现再一次路由的分离, 你可以在api.py中添加你的api路由

#### 注册application

在`pkg-frontend.py`中, 注册application

```python
APPLICATION_LIST = [
    "在这里添加你的application名"
]
```

### 自动创建

- 注意:你的application名, 需要和你在vue中创建的application名一致,路径名(`/frotend/src/pages/appplication名`目录下)
  也需要一致,区分大小写

### 编译以及运行

在编写完vue application后, 运行`pkg-frontend.py`脚本, 编译vue application
编译完成后,就可以直接启动django了
