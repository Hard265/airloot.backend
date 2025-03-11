from rest_framework import serializers
from .models import Partition, Folder, File

class PartitionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Partition
        fields = ['id', 'user', 'name', 'size', 'created_at']

class FolderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'partition', 'parent_folder', 'name', 'created_at']

class FileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = File
        fields = ['id', 'folder', 'name', 'size', 'created_at']
