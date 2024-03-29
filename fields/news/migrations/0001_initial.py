# Generated by Django 5.0.1 on 2024-01-09 13:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('short_title', models.CharField(max_length=200, verbose_name='Краткий заголовок')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('short_descr', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('descr', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время публикации')),
                ('photo', models.ImageField(upload_to='news_&_articles/', verbose_name='Фото')),
                ('preview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news_preview')),
            ],
            options={
                'verbose_name': 'Новость - Статья',
                'verbose_name_plural': 'Новости - Статьи',
                'ordering': ['title'],
            },
        ),
    ]
