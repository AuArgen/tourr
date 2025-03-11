from django.contrib import admin

from post.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'count_days', 'count_ranking', 'price')
    search_fields = ('title',)
    list_filter = ('city', 'count_days', 'count_ranking', 'price')