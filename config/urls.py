from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static

from drive.views import FolderViewSet, FileViewSet
from accounts.views import WhoAmIView, StorageInfoView, UserViewSet

router = routers.DefaultRouter()
router.register("folders", FolderViewSet, basename="folder")
router.register("files", FileViewSet, basename="file")
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("api/v1/whoami/", WhoAmIView.as_view(), name="whoami"),
    path("api/v1/details/", StorageInfoView.as_view(), name="details"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
