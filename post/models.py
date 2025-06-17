import os
import uuid
from ckeditor.fields import RichTextField
from django.db import models

from city.models import City


# Create your models here.

def unique_image_path(instance, filename):
    """
    Генерирует уникальное имя файла для изображения.
    """
    ext = filename.split('.')[-1]  # Получаем расширение файла
    unique_filename = f"{uuid.uuid4().hex}.{ext}"  # Генерируем уникальное имя
    return os.path.join('images/', unique_filename)  # Указываем путь

class Post(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to=unique_image_path, verbose_name='Картинка')
    count_ranking = models.CharField(max_length=20, verbose_name='Рейтинг')
    is_popular = models.BooleanField(default=False, verbose_name='Популярный')
    is_trending = models.BooleanField(default=False, verbose_name='Тренд')
    count_days = models.IntegerField(default=3, verbose_name='На сколько дней')
    price = models.CharField(max_length=50, verbose_name='Цена')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Order(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Емайл')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')

    class Meta:
        verbose_name = 'Брон'
        verbose_name_plural = 'Броны'

    def __str__(self):
        return self.name