from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Partition, Folder, File
from .serializers import PartitionSerializer, FolderSerializer, FileSerializer

class PartitionViewSet(viewsets.ModelViewSet):
    queryset = Partition.objects.all()
    serializer_class = PartitionSerializer
    permission_classes = [IsAuthenticated]

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
