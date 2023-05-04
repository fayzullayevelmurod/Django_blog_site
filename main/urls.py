from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('article/<int:id>/detail', views.article_detail, name='article_detail'),
]
