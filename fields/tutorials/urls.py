from django.urls import path
from .views import tutorials, sub_tutorials, articles_list, article

app_name = 'tutorials'

urlpatterns = [
    path("", tutorials, name="tutorials_list"),
    path('<str:title>/', sub_tutorials, name='sub_tutorials'),
    path('<str:title>/<str:sub_title>/',articles_list, name = "articles-list"),
    path('<str:title>/<str:sub_title>/<str:article_title>/', article, name='article'),
]
