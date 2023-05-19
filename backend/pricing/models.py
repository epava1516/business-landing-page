from django.db import models
from backend.home.models import SingletonModel

class Pricing(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class Action(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class PricingColumn(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class ActionItem(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    column = models.ForeignKey(PricingColumn, on_delete=models.CASCADE, related_name='actions')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.action.description
