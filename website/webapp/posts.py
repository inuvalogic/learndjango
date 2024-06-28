from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Blog, Category

def index(request):
    latest_blog_list = Blog.objects.order_by("-pub_date")[:5]
    categories = Category.objects.all()
    template = loader.get_template("blog/index.html")
    context = {
        "categories": categories,
        "latest_blog_list": latest_blog_list,
    }
    return HttpResponse(template.render(context, request))

def index_alt(request):
    latest_blog_list = Blog.objects.order_by("-pub_date")[:5]
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "latest_blog_list": latest_blog_list,
    }
    return render(request, "blog/index.html", context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {"blog": blog})

def newpost(request):
    b = Blog(
            category_id=request.POST["category_id"],
            title=request.POST["title"],
            content=request.POST["content"],
            pub_date=timezone.now(),
            hits_view=0
        )
    b.save()

    return HttpResponseRedirect(reverse("posts:post-index-alt"))