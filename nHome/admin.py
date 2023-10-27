from django.contrib import admin
from .models import Category, Post


# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'image_tag', 'title', 'description', 'url', 'add_date',)
    search_fields = ('title',)
    list_per_page = 50


# for configuration of Post admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'url', 'cat', 'image_tago',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50


# Register your models here.
admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)
