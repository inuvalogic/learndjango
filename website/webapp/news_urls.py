from django.urls import path

from . import news

app_name = 'news'
urlpatterns = [
    path("category/<str:category_slug>/", news.by_category, name="news-by-category"),
    path("<str:news_slug>", news.detail, name="news-detail"),
]
