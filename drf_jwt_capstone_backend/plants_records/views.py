from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plant_Record
from .serializers import Plant_RecordSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def all_records(request):
    records = Plant_Record.objects.all()
    serializer = Plant_RecordSerializer(records, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_plant_record(request, id):
    plant_record = Plant_Record.objects.filter(id = id)
    serializer =Plant_RecordSerializer(plant_record, many =True)
    return Response(serializer.data)
