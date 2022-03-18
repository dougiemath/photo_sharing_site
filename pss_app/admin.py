from django.contrib import admin
from pss_app.models import Post, Comment

"""
Post section for admin area
"""


@admin.register(Post)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'author', 'tags')
    list_filter = ('title', 'created_on', 'tags')
    search_fields = ('title', 'content', 'tags', 'created_on')


"""
Comment section for admin area
"""


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
