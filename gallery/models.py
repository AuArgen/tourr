import os
import uuid
from ckeditor.fields import RichTextField
from django.db import models

def unique_image_path(instance, filename):
    """
    Генерирует уникальное имя файла для изображения.
    """
    ext = filename.split('.')[-1]  # Получаем расширение файла
    unique_filename = f"{uuid.uuid4().hex}.{ext}"  # Генерируем уникальное имя
    return os.path.join('images/', unique_filename)  # Указываем путь

class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to=unique_image_path, verbose_name='Картинка')
    is_show = models.BooleanField(default=False, verbose_name='Добавить на главный')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title
