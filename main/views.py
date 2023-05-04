from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    articles = Article.objects.filter(is_active = True)
    return render(request, 'home.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    articles = Article.objects.filter(is_active = True)
    return render(request, 'detail.html', {'article': article, 'articles': articles }) 