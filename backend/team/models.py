from django.db import models
from backend.home.models import SingletonModel

class TeamUser(models.Model):
    img_url = models.CharField(max_length=50)
    title = models.CharField(max_length=50, db_index=True)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    type = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

class Team(SingletonModel):
    description = models.TextField()
    list_description = models.ManyToManyField(TeamUser)

    def __str__(self):
        return self.description[:50]
