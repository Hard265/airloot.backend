from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, StorageInfoSerializer
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class StorageInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = StorageInfoSerializer(request.user)
        return Response(serializer.data)

