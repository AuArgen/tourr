# Generated by Django 5.1.6 on 2025-03-11 05:17

import ckeditor.fields
import django.db.models.deletion
import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0002_city_is_show_alter_city_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to=post.models.unique_image_path, verbose_name='Картинка')),
                ('count_ranking', models.CharField(max_length=20, verbose_name='Рейтинг')),
                ('is_popular', models.BooleanField(default=False, verbose_name='Популярный')),
                ('is_trending', models.BooleanField(default=False, verbose_name='Тренд')),
                ('count_days', models.ImageField(default=3, upload_to='', verbose_name='На сколько дней')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
