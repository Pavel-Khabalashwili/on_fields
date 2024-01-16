from django.urls import path, include
from .views import index



app_name = 'index'

urlpatterns = [
    path("", index, name="index"),
    path("tutorials/", include("tutorials.urls")),
    path("news/", include("news.urls")),
]


