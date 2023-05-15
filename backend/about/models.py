from django.db import models

# Create your models here.

class AboutList(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item

class About(models.Model):
    first_description = models.TextField()
    second_description = models.TextField()
    list_description = models.ForeignKey(AboutList, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_description

class Why(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class WhyList(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class SkillList(models.Model):
    title = models.CharField(max_length=20)
    ratio = models.IntegerField()

    def __str__(self):
        return self.title
