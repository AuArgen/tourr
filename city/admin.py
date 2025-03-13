from django.contrib import admin

from city.models import City, About


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'count_tours', 'is_show')
    search_fields = ('title',)
    list_filter = ('is_show',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
