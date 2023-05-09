from django.db import models

# Create your models here.
class about_list(models.Model):
    item = models.CharField(max_length=50)

class about(models.Model):
    first_description = models.TextField()
    second_description = models.TextField()
    list_description = models.ForeignKey(about_list, on_delete=models.CASCADE)

class about_faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class about_faq_list(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class about_skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class about_skill_list(models.Model):
    title = models.CharField(max_length=20)
    ratio = models.IntegerField()
