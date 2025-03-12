from django.contrib import admin

from post.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_days', 'count_ranking', 'price', 'is_popular', 'is_trending')
    search_fields = ('title',)
    list_filter = ('city', 'count_days', 'is_popular', 'is_trending')
