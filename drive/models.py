import uuid
from django.db import models
from accounts.models import User

class Partition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.BigIntegerField()  # Size in bytes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partition = models.ForeignKey(Partition, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.BigIntegerField()  # Size in bytes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
