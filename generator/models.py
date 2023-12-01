from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=200)
    name = models.CharField(max_length=25)
