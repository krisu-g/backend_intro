from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


# Many to many
class Movie(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Character(models.Model):
    name = models.CharField(max_lenght=50)
    actor_name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f'{self.title}'
