from django.urls import path, re_path, register_converter, include

from . import views

urlpatterns = [
    path("path1", views.other_path, name="otherpath1"),
    path("path2", views.other_path, name="otherpath2"),
    path("path3", views.other_path, name="otherpath3"),
]
