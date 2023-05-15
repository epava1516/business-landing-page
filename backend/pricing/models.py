from django.db import models
from backend.home.models import SingletonModel

# Create your models here.
class Pricing(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]
    
class PricingDescriptionList(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

class PricingList(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    price = models.IntegerField()
    descriptionlist = models.ForeignKey(PricingDescriptionList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title