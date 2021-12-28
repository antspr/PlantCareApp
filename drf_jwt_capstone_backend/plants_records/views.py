from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plant_Record
from .serializers import Plant_RecordSerializer
from django.contrib.auth.models import User

class Plant_RecordList(APIView):

    permission_classes = [AllowAny]

    def get (self, request):
        plant_records = Plant_Record.objects.all()
        serializer = Plant_RecordSerializer(plant_records, many=True)
        return Response(serializer.data)
