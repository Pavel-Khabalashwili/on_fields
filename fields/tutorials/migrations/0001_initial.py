# Generated by Django 5.0.1 on 2024-01-09 06:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('short_descr', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('descr', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='tutorial/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tutorial_subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('short_descr', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('descr', models.TextField(verbose_name='Описание')),
                ('id_tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='tutorials.tutorial')),
            ],
            options={
                'verbose_name': 'Подраздел',
                'verbose_name_plural': 'Подразделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('short_descr', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('descr', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время публикации')),
                ('id_subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='tutorials.tutorial_subsection')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['title'],
            },
        ),
    ]
