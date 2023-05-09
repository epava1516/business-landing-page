from django.db import models

# Create your models here.
class team(models.Model):
    description = models.TextField()

class team_user(models.Model):
    img_url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
