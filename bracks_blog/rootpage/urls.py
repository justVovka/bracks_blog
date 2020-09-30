from django.urls import path

from . import views

app_name = 'rootpage'

urlpatterns = [
    path('', views.index, name='index'),
]
