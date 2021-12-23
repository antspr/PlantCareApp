from django.db import models
from django.contrib.auth import get_user_model


#from django.db.models import 




User=get_user_model()


#import plant model to get user plant?
#Using user import to drill down to user/plant/history
#use tutorial to set up user and may have to make get_user_plants function to get plant specific history

class Plant_Record(models.Model):
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE) #How to get FK without user model?
    date_of_activity = models.DateTimeField # check formatting for display issues like in previous project.
    activity_notes = models.CharField(max_length=500)
    didWater = models.NullBooleanField
    didChangeDirt = models.NullBooleanField
    didRotate = models.NullBooleanField


