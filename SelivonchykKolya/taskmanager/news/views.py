from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'news/index.html')


def about(request):
    return render(request, 'news/news.html')


def user(request):
    return render(request, 'news/user.html')
