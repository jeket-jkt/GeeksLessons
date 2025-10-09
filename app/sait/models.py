from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    facebook = models.URLField(
        verbose_name='FaceBook',
        help_text='URL FaceBook'
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        help_text='URL Twitter'
    )
    github = models.URLField(
        verbose_name='GitHub',
        help_text='URL GitHub'
    )
    google = models.URLField(
        verbose_name='Google',
        help_text='URL Google'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class Statics(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    statics = models.IntegerField(
        verbose_name='Статистика'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'    


class Imgaes(models.Model):
    image = models.ImageField(
        upload_to='images',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.text[:30]}"