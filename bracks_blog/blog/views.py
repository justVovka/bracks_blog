from django.http import HttpResponse

from .models import Article


def index(request):
    articles = Article.objects.filter(is_published=True)
    output = ', '.join([article.link for article in articles])
    return HttpResponse(output)
