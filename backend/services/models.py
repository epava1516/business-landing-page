from django.db import models
from backend.home.models import SingletonModel

class ServiceList(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Services(SingletonModel):
    description = models.TextField()
    list_description = models.ManyToManyField(ServiceList)

    def __str__(self):
        return self.description[:50]

class Cta(SingletonModel):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title
