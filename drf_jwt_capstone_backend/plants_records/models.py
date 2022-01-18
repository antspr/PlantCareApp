from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()


#import plant model to get user plant?
#Using user import to drill down to user/plant/history
#use tutorial to set up user and may have to make get_user_plants function to get plant specific history

class Plant_Record(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE) #How to get FK without user model?
    date_of_activity = models.DateTimeField # check formatting for display issues like in previous project.
    activity_notes = models.CharField(max_length=500)
    didWater = models.BooleanField(null=True)
    didChangeDirt = models.BooleanField(null=True)
    didRotate = models.BooleanField(null=True)
    
    
    def __str__(self) -> str:
        return self.plant.plant_name

