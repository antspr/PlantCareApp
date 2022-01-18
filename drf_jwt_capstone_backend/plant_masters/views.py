from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plants_Master
from .serializers import Plants_MasterSerializer
from django.contrib.auth import get_user

@api_view(['GET'])
@permission_classes([AllowAny])

def master_plant_list(request):
    plant_masters = Plants_Master.objects.all()
    serializer = Plants_MasterSerializer(plant_masters, many=True)
    return Response(serializer.data)


#Currently Adding new master plant through admin site-- is use case for user to add new plant to list
api_view(['POST'])
permission_classes([IsAuthenticated])
def new_master(request):
   serializer = Plants_MasterSerializer(data = request.data)
   if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def master_by_id(request, id):
    master_plant = Plants_Master.objects.filter(id = id)
    serializer = Plants_MasterSerializer(master_plant, many = True)
    return Response(serializer.data)
    
   
