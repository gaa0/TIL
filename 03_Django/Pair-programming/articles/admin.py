from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)