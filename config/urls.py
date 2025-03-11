from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from drive.views import PartitionViewSet, FolderViewSet, FileViewSet

router = routers.DefaultRouter()
router.register("partitions/", PartitionViewSet, basename="partition")
router.register("folders/", FolderViewSet, basename="folder")
router.register("files/", FileViewSet, basename="file")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("admin/", admin.site.urls),
]
