from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Tutorial_subsection, Article

def tutorials(request: HttpRequest):
    context = {
        "tutorials": Tutorial.objects.all(),
    }
    return render(request, "tutorials/tutorials.html", context)

def sub_tutorials(request: HttpRequest, title: str):
    tutorial = get_object_or_404(Tutorial, title=title)
    subsections = tutorial.subsections.all()
    context = {
        "tutorial": tutorial,
        "subsections": subsections,
    }
    return render(request, "tutorials/sub-tutorials.html", context)

def articles_list(request: HttpRequest, title: str, sub_title: str):
    tutorial = get_object_or_404(Tutorial, title=title)
    subsection = Tutorial_subsection.objects.get(title=sub_title)
    context = {
        "tutorial": tutorial,
        "subsection": subsection,
        "articles": subsection.articles.all(),
    }
    return render(request, "tutorials/articles-list.html", context)

def article(request: HttpRequest, title:str, sub_title:str, article_title:str):
    tutorial = get_object_or_404(Tutorial, title=title)
    subsection = Tutorial_subsection.objects.get(title=sub_title)
    article = Article.objects.get(title=article_title)
    context = {
        "subsection": subsection,
        "tutorial": tutorial,
        'article': article,
    }
    return render(request, "tutorials/article.html", context)