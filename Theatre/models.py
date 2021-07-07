from datetime import timezone, date
from functools import partial
from django.db.models import Q
from django.db import models

# Create your models here.
class Actors(models.Model):
    Surname=models.CharField(max_length=255, verbose_name="Фамилия")
    Name=models.CharField(max_length=255, verbose_name="Имя")
    Father_name=models.CharField(max_length=255, verbose_name="Отчество")
    Photo = models.ImageField(upload_to="photos", null=True, verbose_name="Фото")
    Experience=models.IntegerField(blank=True, null=False, verbose_name="Стаж")
    Age=models.IntegerField(blank=True, null=False , verbose_name="Возраст")
    Phone=models.CharField(max_length=14, null=True, verbose_name="Номер телефона")
    Bio=models.TextField(blank=True, null=True, verbose_name="Биография")

    def __str__(self):
        return (self.Surname+" "+self.Name)

    class Meta:
        verbose_name='Актеры театра'
        verbose_name_plural = 'Актеры театра'
        ordering = ['Surname','Name']



class Amplua(models.Model):
    Actor=models.ForeignKey('Actors', on_delete=models.CASCADE)
    Play=models.ForeignKey('Plays', on_delete=models.CASCADE)
    Role=models.CharField(max_length=255)

    def __str__(self):
        return (self.Role)



    class Meta:
        verbose_name='Амплуа актера'
        verbose_name_plural = 'Амплуа актеров'
        ordering = ['Role']

class Plays(models.Model):
    Title=models.CharField(max_length=255, verbose_name="Название")
    Director=models.CharField(max_length=255, verbose_name="Режиссер")
    Author=models.CharField(max_length=255, verbose_name="Автор")
    Picture = models.ImageField(upload_to="photos", null=True, verbose_name="Афиша")
    About = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return (self.Title)

    class Meta:
        verbose_name='Пьеса'
        verbose_name_plural = 'Пьесы'
        ordering = ['Title']

class Staging(models.Model):
    Staging=models.ForeignKey('Plays', on_delete=models.CASCADE)
    Date=models.DateField(blank=True, default=date.today)


    class Meta:
        verbose_name='Постановка'
        verbose_name_plural = 'Постановки'


class Tickets(models.Model):
    Price=models.IntegerField()
    Place=models.IntegerField()

    def __str__(self):
        return (self.Place)

    class Meta:
        verbose_name='Билет'
        verbose_name_plural = 'Билеты'

