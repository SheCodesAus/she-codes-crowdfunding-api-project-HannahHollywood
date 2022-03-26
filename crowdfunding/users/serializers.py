from pydoc import describe
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class BadgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    image = serializers.URLField()
    description = serializers.CharField(max_length=50)
    badge_type = serializers.CharField(max_length=50)
    user = serializers.IntegerField()