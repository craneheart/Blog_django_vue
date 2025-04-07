# Blog_django_vue

[简体中文](./README.md) | English

## Introduction

A solution using Django as the back-end and Vue.js as the front-end framework for Multi-Page Applications (MPA).

## Highlights

- Provide a Vue3 MPA template/boilerplate solution.

- Propose a standardized routing structure (approach) for integrating Django with Vue3 in MPA scenarios, including
  front-end application configuration.

- Utilize Python automation scripts to compile and update the application’s static assets automatically.

## Template Structure Explanation

### Django

Under the project root directory, the structure is as follows:

```
--backend
  |--> application 1
  |--> application 2
  ... ...
  |--> static # Static files directory
  |--> vue    # Directory for Vue applications
  |--> manage.py
```

- `static`: Stores static files. Compiled Vue assets (e.g., JS, CSS) are placed here.

- `vue`: Acts as the entry point for Django to integrate and reference Vue applications.

#### Vue Template Entry in Django

The Vue directory structure is as follows:

```
--vue
  |--> default
  |--> vue_application_1
    |--> index.html
  |--> vue_application_2
    |--> index.html
  ... ...
  |--> application.json
  |--> vue.py
```

- **`default`**: Stores default pages returned when `vue.py` cannot locate the application.
- **`index.html`**: Entry point HTML file for a Vue application.
- **`application.json`**: Auto-generated Vue application registration JSON file (created by running `pkg-frontend.py`).
- **`vue`**: Main package that simplifies route registration for `index.html`.

### Vue3

Page configurations are set in `vite.config.js`, and the `src` directory structure is as follows:

```
--src
  |--> assets
  |--> components # Common components
  |--> pages
    |--> application_1 # One of the multi-page applications
      |--> components
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

## Usage

Create a new Vue + Django application

### Manual Creation

#### Create Vue Application

Based on the above Vue3 structure, create a new Vue application, where index.html, main.js, router/index.js,
store/index.js, App.vue, and other files need to be created manually.

Then start setting up the Django application

1. Add the application in `settings.py`
2. Add the application's route in `backend/urls.py`
3. Enable the following settings in `your application path/urls.py`

```python
from django.urls import path, include, re_path
from .views import api
from vue.vue import Index

urlpatterns = [
    re_path(r'^(?!api/).*$', Index.get("your application name")),
    path("api/", include(api)),
]
```

4. In your application name/views.py, enable the following settings

Create an api.py with the following routes

```python
from django.urls import path

urlpatterns = [

]
```

- In this way, achieving another level of route separation, you can add your API routes in `api.py`.

#### Register application

Register the application in `pkg-frontend.py`.

```python
APPLICATION_LIST = [
    "Add your application name here"
]
```

### Automatic Creation

Use the `pkg-frontend.py` script to automatically create a Vue application and a Django application.
Run the script directly, enter the application name as prompted, and it will automatically create the Vue application
and the Django application.

- Note: Your application name needs to be consistent with the application name you created in Vue, and the path name (
  under the `/frontend/src/pages/application_name` directory) also needs to be consistent, case-sensitive.

### Compilation and Execution

After writing the Vue application, run the `pkg-frontend.py` script to compile the Vue application.
Once the compilation is complete, you can directly start Django.