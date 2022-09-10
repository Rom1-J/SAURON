from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    url = serializers.StringRelatedField(
        source="get_absolute_url", read_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "language",
            "theme",
            "url",
        ]

        read_only_fields = ["username", "email"]
