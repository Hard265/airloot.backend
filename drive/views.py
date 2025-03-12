from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Partition, Folder, File
from rest_framework.exceptions import PermissionDenied
from .serializers import PartitionSerializer, FolderSerializer, FileSerializer


class PartitionViewSet(viewsets.ModelViewSet):
    queryset = Partition.objects.all()
    serializer_class = PartitionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(partition__user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data["subfolders"] = FolderSerializer(instance.subfolders.all(), many=True).data
        data["files"] = FileSerializer(instance.file_set.all(), many=True).data
        return Response(data)

    def perform_create(self, serializer):
        partition = serializer.validated_data["partition"]
        if partition.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to add folders to this partition."
            )
        serializer.save()

    def perform_update(self, serializer):
        partition = serializer.validated_data["partition"]
        if partition.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to update folders in this partition."
            )
        serializer.save()


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(folder__partition__user=self.request.user)

    def perform_create(self, serializer):
        folder = serializer.validated_data["folder"]
        if folder.partition.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to add files to this folder."
            )
        serializer.save()

    def perform_update(self, serializer):
        folder = serializer.validated_data["folder"]
        if folder.partition.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to update files in this folder."
            )
        serializer.save()
