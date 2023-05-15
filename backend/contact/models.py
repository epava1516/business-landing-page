from django.db import models
from backend.home.models import SingletonModel

# Create your models here.
class Contact(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]
    
class Card(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]