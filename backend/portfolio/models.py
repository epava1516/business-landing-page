from django.db import models
from backend.home.models import SingletonModel

class Portfolio(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class PortfolioItemList(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    type = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title
