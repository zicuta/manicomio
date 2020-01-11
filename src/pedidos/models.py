from django.db import models

class Comanda(models.Model):
    orden=models.CharField(max_length=120)
# Create your models here.
