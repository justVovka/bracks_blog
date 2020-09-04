from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
