from django.urls import path

from . import posts_generic

app_name = 'posts'
urlpatterns = [
    path("all", posts_generic.IndexView.as_view(), name="post-index-alt"),
    path("<int:pk>", posts_generic.DetailView.as_view(), name="post-detail"),
    path("new", posts_generic.Newpost.as_view(), name="new-post"),
]
