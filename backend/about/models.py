from django.db import models
from backend.home.models import SingletonModel

# Create your models here.

class AboutList(models.Model):
    item = models.TextField()

    def __str__(self):
        return self.item

class About(SingletonModel):
    first_description = models.TextField()
    second_description = models.TextField()
    list_description = models.ManyToManyField(AboutList)

    def __str__(self):
        return self.first_description

class WhyList(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Why(SingletonModel):
    title = models.CharField(max_length=100, db_index=True)
    title_bold = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    list_description = models.ManyToManyField(WhyList)

    def __str__(self):
        return self.title

class SkillList(models.Model):
    title = models.CharField(max_length=100)
    ratio = models.IntegerField()

    def __str__(self):
        return self.title

class Skill(SingletonModel):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    list_description = models.ManyToManyField(SkillList)

    def __str__(self):
        return self.title
