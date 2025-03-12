from django.contrib import admin
from .models import Partition, Folder, File


@admin.register(Partition)
class PartitionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "size", "created_at")
    list_filter = ("created_at",)
    raw_id_fields = ("user",)
    search_fields = ("user__email", "name")
    ordering = ("-created_at",)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "partition", "parent_folder", "name", "created_at")
    list_filter = ("partition", "created_at")
    raw_id_fields = ("partition", "parent_folder")
    search_fields = ("name", "partition__name", "partition__user__email")
    ordering = ("-created_at",)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "folder", "name", "file", "size", "created_at")
    list_filter = ("folder", "created_at")
    raw_id_fields = ("folder",)
    search_fields = ("name", "folder__name", "folder__partition__user__email")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    def size(self, obj):
        return obj.size()
