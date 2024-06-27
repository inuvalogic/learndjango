from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def list_by_category(request):
    return HttpResponse("list_by_category")

def list_by_year(request, year):
    return HttpResponse("list_by_year " + str(year))

def list_by_month(request, year, month):
    return HttpResponse("list_by_month " + str(year) + " " + str(month))

def post_detail(request, year, month, slug):
    return HttpResponse("post_detail " + str(year) + " " + str(month) + " " + str(slug))

def path_converter_string(request, param_str):
    return HttpResponse("path_converter_string " + str(param_str))

def path_converter_number(request, param_int):
    return HttpResponse("path_converter_number " + str(param_int))

def path_converter_slug(request, param_slug):
    return HttpResponse("path_converter_slug " + str(param_slug))

def path_converter_uuid(request, param_uuid):
    return HttpResponse("path_converter_uuid " + str(param_uuid))

def path_converter_path(request, param_path):
    return HttpResponse("path_converter_path " + str(param_path))

def regex(request, page_number):
    return HttpResponse("regex " + str(page_number))

def list_custom(request, year):
    return HttpResponse("list_custom " + str(year))

def page(request, num=1):
    return HttpResponse("page " + str(num))

def articles(request):
    return HttpResponse("article list")

def other_path(request):
    return HttpResponse("other_path")
