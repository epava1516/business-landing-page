from django.db import models

# Create your models here.
class services(models.Model):
    description = models.TextField()

class service_list(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

class service_contact(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
