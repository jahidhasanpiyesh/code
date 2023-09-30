from django.db import models


# Create your models here.
class profile(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    collage = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    skill = models.TextField(max_length=200)
    about_you = models.TextField(max_length=500)
    previews_work = models.TextField(max_length=300)

