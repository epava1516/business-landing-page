from django.db import models
from backend.home.models import SingletonModel

# Create your models here.
class Faq(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class FaqList(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title