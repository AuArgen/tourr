from django.contrib import admin

from city.models import City


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'count_tours', 'is_show')
    search_fields = ('title', )
    list_filter = ('is_show', )
