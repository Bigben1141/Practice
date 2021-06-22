from django.db import models

# Create your models here.
class Actors(models.Model):
    Surname=models.CharField(max_length=255)
    Name=models.CharField(max_length=255)
    Father_name=models.CharField(max_length=255)
    Photo = models.ImageField(upload_to="photos", null=True)
    Experience=models.IntegerField(blank=True, null=False)
    Age=models.IntegerField(blank=True, null=False)
    Phone=models.CharField(max_length=14, null=True)
    Bio=models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.Surname+" "+self.Name)

    class Meta:
        verbose_name='Актеры театра'
        verbose_name_plural = 'Актеры театра'
        ordering = ['Surname','Name']


class Amplua(models.Model):
    Actor=models.ForeignKey('Actors', on_delete=models.CASCADE)
    Role=models.CharField(max_length=255)

    def __str__(self):
        return (self.Role)