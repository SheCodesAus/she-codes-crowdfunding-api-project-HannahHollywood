from pydoc import describe
from rest_framework import serializers
from .models import CustomUser, Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)



# User Profile Serializer
class ProfileSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=600)
    avatar = serializers.URLField()
    bio = serializers.CharField(max_length=600)
    website = serializers.URLField()

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)


class ProfileDetailSerializer(ProfileSerializer):
        # pledges = ProfileSerializer(many=True, read_only=True)

        def update(self, instance, validated_data):
            instance.full_name = validated_data.get('full name',instance.full_name)
            instance.avatar = validated_data.get('avatar', instance.avatar)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.website = validated_data.get('website', instance.website)
            instance.save()
            return instance


class BadgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    image = serializers.URLField()
    description = serializers.CharField(max_length=50)
    badge_type = serializers.CharField(max_length=50)
    user = serializers.IntegerField()


# CREATE A USER ACCOUNT
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user