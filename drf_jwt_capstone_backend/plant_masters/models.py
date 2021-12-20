from django.db import models


# Create your models here.
class Plants_Master(models.Model):
    plant_name = models.CharField(max_length=25)
    care_instructions = models.CharField(max_length=500)
