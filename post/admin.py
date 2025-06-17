from django.contrib import admin

from post.models import Post, Order


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_days', 'count_ranking', 'price', 'is_popular', 'is_trending')
    search_fields = ('title',)
    list_filter = ('city', 'count_days', 'is_popular', 'is_trending')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_post_title', 'name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

    def get_post_title(self, obj):
        return obj.post.title

    get_post_title.short_description = 'Пост'