from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Factory, Bike


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'website', 'show_bikes', 'image_thumbnail']

    def show_bikes(self, obj):
        bikes = obj.bike_set.all()
        return ', '.join([p.model_name for p in bikes])

    show_bikes.short_description = 'Модели в категории'

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' height='150px' width=260>")
        else:
            return 'Нет изображения'

    image_thumbnail.short_description = 'Изображение'


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['factory', 'model_name', 'engine_volume', 'year', 'get_readable_filename', 'file_preview_thumbnail']

    def file_preview_thumbnail(self, obj):
        if obj.file_preview:
            return mark_safe(f"<img src='{obj.file_preview.url}' height='50px' width=50>")
        else:
            return 'Нет изображения'

    file_preview_thumbnail.short_description = 'Превью'
