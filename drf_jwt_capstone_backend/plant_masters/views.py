from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plants_Master
from .serializers import Plants_MasterSerializer
from django.contrib.auth.models import User

class Plants_MastersList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        plant_masters = Plants_Master.objects.all()
        serializer = Plants_MasterSerializer(plant_masters, many=True)
        return Response(serializer.data)
