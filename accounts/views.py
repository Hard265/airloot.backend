from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, StorageInfoSerializer
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]

    def list(self, request):
        if bool(request.user and request.is_authenticated):
            self.queryset.filter(email=request.user.email)


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
