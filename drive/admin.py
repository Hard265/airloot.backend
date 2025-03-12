from django.contrib import admin
from .models import Partition, Folder, File

admin.site.register(Partition)
admin.site.register(Folder)
admin.site.register(File)
