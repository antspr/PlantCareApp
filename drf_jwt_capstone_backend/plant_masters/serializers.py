from rest_framework import serializers
from .models import Plants_Master

class Plants_MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants_Master
        fields = ('plant_name', 'care_instructions')