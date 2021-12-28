from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plant
from .serializers import PlantSerializer
from django.contrib.auth import get_user

class PlantList(APIView):

    permission_classes= [IsAuthenticated]

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
