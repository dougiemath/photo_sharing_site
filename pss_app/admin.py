from django.contrib import admin
from pss_app.models import Post

# Register your models here.

@admin.register(Post)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'author','tags')
    list_filter = ('title', 'created_on', 'tags')
    search_fields = ('title', 'content', 'tags', 'created_on')
    

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on')