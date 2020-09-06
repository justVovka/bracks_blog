from django.shortcuts import render

from .models import Article, Category


def index(request):
    articles = Article.objects.filter(is_published=True)
    categories = Category.objects.all()
    return render(request, 'blog/index.html', locals())
