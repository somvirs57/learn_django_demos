from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    standard = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    def __str(self):
        return self.name