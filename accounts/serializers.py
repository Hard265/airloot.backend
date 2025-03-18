from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email"]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            if not user:
                raise AuthenticationFailed(
                    _("Unable to log in with provided credentials.")
                )

        else:
            raise serializers.ValidationError(_('Must include "email" and "password".'))

        data["user"] = user
        return data


class StorageInfoSerializer(serializers.ModelSerializer):
    used_storage = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ["quota", "used_storage"]

    def get_used_storage(self, obj):
        return sum(file.size for file in obj.files.all())
