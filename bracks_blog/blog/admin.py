from django.contrib import admin

from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
