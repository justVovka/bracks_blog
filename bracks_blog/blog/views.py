from django.shortcuts import render

from .models import Article, Category


def index(request):
    articles = Article.objects.filter(is_published=True)
    categories = Category.objects.all()
    return render(request, 'blog/index.html', locals())


def single_article(request, article_link):
    article = Article.objects.get(link=article_link)
    categories = Category.objects.all()
    return render(request, 'blog/article.html', locals())


def about(request):
    categories = Category.objects.all()
    return render(request, 'blog/about.html', locals())
