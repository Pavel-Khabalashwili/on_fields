from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import FAQ
from  tutorials.models import Tutorial
from news.models import News_preview



def index(request: HttpRequest):
    context = {
        "faqs" : FAQ.objects.all(),
        "tutorials": Tutorial.objects.all(),
        "news" :  News_preview.objects.all(),
    }
    return render(request, 'index/index.html', context)