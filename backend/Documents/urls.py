from django.urls import path, include, re_path
from .views import api
from vue.vue import Index

urlpatterns = [
    re_path(r'^(?!api/).*$', Index.get("Documents")),
    path("api/", include(api)),
]
