from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse("user profile")

def password(request):
    return HttpResponse("user password")

def setting(request):
    return HttpResponse("user setting")

