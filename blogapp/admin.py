from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    fields = ['id','title', 'body','categories', 'postimage']

admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['id','name']

admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    fields = ['id','author', 'body', 'created','updated','post']


