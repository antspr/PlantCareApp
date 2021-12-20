from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # master_plant = models.ForeignKey(MasterPlant, on_delete=models.CASCADE)
    isActive = False
    
    
