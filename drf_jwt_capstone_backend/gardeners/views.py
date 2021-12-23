from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gardener
from .serializers import GardenerSerializer
from django.contrib.auth.models import User

class GardenerList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        gardeners = Gardener.objects.all()
        serializer = GardenerSerializer(gardeners, many=True)
        return Response(serializer.data)