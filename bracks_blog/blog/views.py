from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Article, Category, Tag


def index(request):
    articles = Article.objects.filter(is_published=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/index.html', locals())


def single_article(request, article_link):
    article = get_object_or_404(Article, link=article_link)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/article.html', locals())


def about(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/about.html', locals())


def articles_by_category(request, category_link):
    current_category = get_object_or_404(Category, link=category_link)
    category_id = current_category.id
    articles = Article.objects.filter(is_published=True, category_id=category_id)
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    paginated_articles = paginator.get_page(page_number)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/articles_by_category.html', locals())


def articles_by_tag(request, tag_link):
    current_tag = get_object_or_404(Tag, link=tag_link)
    tag_id = current_tag.id
    articles = Article.objects.filter(is_published=True, tags__in=[tag_id])
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    paginated_articles = paginator.get_page(page_number)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/articles_by_tag.html', locals())