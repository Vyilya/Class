from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=250, verbose_name="ФИО", blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    vk = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return f"{self.title}, {self.text}"


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=340, verbose_name="Описание")
    article = models.ManyToManyField(Article, verbose_name="Статья")

    def __str__(self):
        return f"{self.title}, {self.article}"

class UserGroup(models.Model):
    group = models.CharField(max_length=250, verbose_name="Группа", blank=True, null=True)
    full_name = models.CharField(max_length=250, verbose_name="ФИО", blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    city = models.CharField(max_length=250, verbose_name="Город", blank=True, null=True)
