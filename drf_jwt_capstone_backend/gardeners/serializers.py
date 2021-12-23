from rest_framework import serializers
from .models import Gardener

class GardenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gardener
        fields = ['id', 'user','email', 'street', 'city', 'state', 'zipcode']
