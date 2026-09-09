from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'), # Maps the app's root URL to the articles view
    path('<int:article_id>/', views.articles_detail, name='articles_detail'), # Maps a URL with an article id to the article_details in the views.py file
]