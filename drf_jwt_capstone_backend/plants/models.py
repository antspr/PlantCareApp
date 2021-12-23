from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Plant(models.Model):
    gardener = models.ForeignKey('gardeners.Gardener', on_delete=models.CASCADE)
    master_plant = models.ForeignKey('plant_masters.Plants_Master', on_delete=models.CASCADE)
    isActive = False
    

