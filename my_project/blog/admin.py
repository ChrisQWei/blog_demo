from django.contrib import admin
from blog.models import blogs

# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'plain_text','post_time' )
    search_fields = ['article_name']


admin.site.register(blogs, BlogsAdmin)