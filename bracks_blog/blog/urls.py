from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<slug:article_link>/', views.single_article, name='article'),
    path('about/', views.about, name='about'),
]
