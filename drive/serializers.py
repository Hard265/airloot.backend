from rest_framework import serializers
from .models import Partition, Folder, File
from django.contrib.auth import get_user_model


class PartitionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="email"
    )

    class Meta:
        model = Partition
        fields = ["id", "user", "name", "size", "created_at"]


class FolderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Folder
        fields = ["id", "partition", "parent_folder", "name", "created_at"]


class FileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = File
        fields = ["id", "folder", "name", "size", "created_at"]
