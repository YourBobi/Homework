from django.shortcuts import render
from django.http import HttpResponse
from RR import MyParser, create_keys, CreateFile
from bs4 import BeautifulSoup

def index(request):
    search_url = request.GET.get('search')
    if search_url:
        rss = MyParser(search_url, keys=create_keys())
        with open('news/templates/news/news.html', 'w', encoding="UTF-8") as file:
            s = """{% extends 'news/index.html' %}
            {% block content %}""" + CreateFile(rss).create_sample_html() + "{% endblock %}"
            file.write(s)

        return render(request, 'news/news.html', {'rss': rss})

    return render(request, 'news/index.html')


def about(request):
    return render(request, 'news/news.html')


def user(request):
    return render(request, 'news/user.html')
