from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    link = models.CharField(max_length=100, default="https://www.google.com")
    location = models.TextField(default="Boston, MA")
    duration = models.CharField(max_length=100, default="2018-present")

    def __str__(self):
        return self.title

class Hobby(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title