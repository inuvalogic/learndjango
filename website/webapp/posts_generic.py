from django.views import generic
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from .models import Blog, Category

class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_blog_list"

    def get_queryset(self):
        return Blog.objects.order_by("-pub_date")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        # context["latest_blog_list"] = Blog.objects.order_by("-pub_date")[:5]
        return context

class DetailView(generic.DetailView):
    model = Blog
    template_name = "blog/detail.html"

class Newpost(generic.CreateView):
    model = Blog
    template_name = 'blog/index.html'
    fields = ["category", "title", "content"]

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        form.instance.hits_view = 0
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["latest_blog_list"] = Blog.objects.order_by("-pub_date")[:5]
        return context