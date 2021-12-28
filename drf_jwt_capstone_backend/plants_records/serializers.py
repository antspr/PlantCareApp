from rest_framework import serializers
from .models import Plant_Record

class Plant_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant_Record
        fields = ['id', 'plant', 'date_of_activity', 'activity_notes', 'didWater', 'didChangeDirt', 'didRotate']