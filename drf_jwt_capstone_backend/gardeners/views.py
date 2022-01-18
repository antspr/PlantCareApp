from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gardener
from .serializers import GardenerSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def register_gardener(request):
    gardener = User.objects.filter(gardener = request.user.id)
    serializer = GardenerSerializer( data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

