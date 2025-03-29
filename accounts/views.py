from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.permissions import IsOwner
from accounts.serializers import RegisterSerializer, UserSerializer


class RegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []  # Allow anyone to register


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return self.request.user
