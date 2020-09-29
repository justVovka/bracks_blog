from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(unique=True, blank=False, null=False, max_length=64)
    link = models.SlugField(unique=True, default='')
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    is_published = models.BooleanField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    category = models.ForeignKey('blog.Category', on_delete=models.PROTECT, null=False)
    tags = models.ManyToManyField('blog.Tag')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(unique=True, null=False, blank=False, max_length=64)
    link = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(unique=True, null=False, blank=False, max_length=64)
    link = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.title
