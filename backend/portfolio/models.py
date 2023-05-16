from django.db import models
from backend.home.models import SingletonModel

class PortfolioItemList(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    type = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

class Portfolio(SingletonModel):
    description = models.TextField()
    list_description = models.ManyToManyField(PortfolioItemList)

    def __str__(self):
        return self.description[:50]
