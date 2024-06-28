from django.urls import path, re_path, register_converter, include

from . import posts

app_name = 'posts'
urlpatterns = [
    path("", posts.index, name="post-index"),
    path("all", posts.index_alt, name="post-index-alt"),
    path("<int:blog_id>", posts.detail, name="post-detail"),
    path("new", posts.newpost, name="new-post"),
]
