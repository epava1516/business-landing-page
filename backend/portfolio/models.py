from django.db import models

# Create your models here.
class portfolio(models.Model):
    description = models.TextField()

class portfolio_item_list(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img_url = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
