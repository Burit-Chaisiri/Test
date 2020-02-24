from django.db import models

# Create your models here.
class Calculate(models.Model):
    x = models.CharField(max_length=20)
    y = models.CharField(max_length=20)