from django.db import models
from django.contrib.auth.models import User

class Actor(models.Model):
    name=models.CharField(max_length=55)
    country=models.CharField(max_length=55)
    gender=models.CharField(max_length=15, choices=(('Male','Male'),
                                                    ('Female','Female')))
    birthdate=models.DateField()


    def __str__(self):
        return self.name


class Movie(models.Model):
    name=models.CharField(max_length=75)
    country=models.CharField(max_length=55)
    ganre=models.CharField(max_length=55)
    year=models.DateField(blank=True,null=True)
    actors=models.ManyToManyField(Actor)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name=models.CharField(max_length=25)
    price=models.PositiveIntegerField()
    duration=models.DurationField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    grade=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user
