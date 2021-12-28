from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.Serializer):
    class Meta:
        model = Plant
        fields = ['id', 'gardener', 'master_plant', 'isActive']