# Generated by Django 5.1.6 on 2025-03-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='count_days',
            field=models.IntegerField(default=3, verbose_name='На сколько дней'),
        ),
    ]
