from django.contrib import admin

from gallery.models import Gallery


# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'is_show')
    search_fields = ('title',)