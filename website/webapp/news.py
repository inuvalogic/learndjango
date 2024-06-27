from django.shortcuts import render
from django.http import HttpResponse

news_data = {
    "title": "kategori berita",
    "news" : [
        {
            "slug": 'berita-1',
            "title": "berita pertama",
            "content": "ini berita pertama"
        },
        {
            "slug": 'berita-2',
            "title": "berita kedua",
            "content": "ini berita kedua"
        }
    ]
}

def by_category(request, category_slug):
    return render(request, "news/category.html", news_data)

def detail(request, news_slug):
    data = next(filter(lambda news: news['slug'] == news_slug, news_data['news']), None)
    return render(request, "news/detail.html", data)
