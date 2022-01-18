from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Plant
from .serializers import PlantSerializer
from django.contrib.auth import get_user
#Get entire list of Plants(junctiontable) to loop through and filter on front end
@api_view(['GET'])
@permission_classes([AllowAny])
def all_plants(request):
    plant = Plant.objects.all()
    serializer = PlantSerializer(plant, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
#Write in masterID for serializer?
def add_plant(request):
    serializer = PlantSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_plants(request, id):
    gardener_plants = Plant.objects.filter(gardener__id = id).first()
    serializer = PlantSerializer(gardener_plants, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_plant_by_id(request, id):
    plant = Plant.objects.filter(id = id)
    serializer = PlantSerializer(plant, many =True)
    return Response(serializer.data)

api_view(['GET'])
permission_classes([IsAuthenticated])
def activate_plant(request, id):
    plants = get_my_plants(id).first()
    plant = plants.filter(id).first()
    serializer = PlantSerializer(plant, many = False)
    if (plant.isActive != True ):
        plant.isActive = True
        serializer = PlantSerializer(plant, many=False)
        if serializer.is_valid():
            plant.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.data, status= status.HTTP_404_NOT_FOUND)

    
