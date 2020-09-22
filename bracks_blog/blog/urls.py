from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/category/<slug:category_link>/', views.articles_by_category, name='articles_by_category'),
    path('blog/tag/<slug:tag_link>/', views.articles_by_tag, name='articles_by_tag'),
    path('blog/<slug:article_link>/', views.single_article, name='article'),
    path('about/', views.about, name='about'),
]
