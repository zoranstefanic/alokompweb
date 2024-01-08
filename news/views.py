from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class NewsList(ListView):
    model = NewsItem
    template_name = "news/newslist.html"
    context_object_name = "news"

class NewsItemDetail(DetailView):
    model = NewsItem
    template_name = "news/newsitem.html"
    context_object_name = "item"
