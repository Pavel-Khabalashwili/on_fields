# Generated by Django 5.0.1 on 2024-02-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]