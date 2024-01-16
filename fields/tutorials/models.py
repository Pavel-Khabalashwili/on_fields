from datetime import datetime 
from django.db import models

# САМОУЧИТЕЛЬ
# Раздел
class Tutorial(models.Model):

    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='tutorial/')

    class Meta:
        ordering = ["title"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.title
    
#Подраздел
class Tutorial_subsection(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    id_tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='subsections', verbose_name='Раздел')

    class Meta:
        ordering = ["title"]
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"

    def __str__(self):
        return self.title

#Cтатьи
class Article(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    short_descr = models.CharField('Краткое описание', max_length=500)
    descr = models.TextField('Описание')
    pub_date = models.DateTimeField('Время публикации', default=datetime.now)
    id_subsection = models.ForeignKey(Tutorial_subsection, on_delete=models.CASCADE, related_name='articles',verbose_name='Подраздел' )
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
