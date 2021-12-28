from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Gardener(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=11, null=True)