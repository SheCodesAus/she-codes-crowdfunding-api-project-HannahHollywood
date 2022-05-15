from pydoc import describe
from rest_framework import serializers

from .models import Badge, CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class BadgeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Badge
        fields = ['id', 'image', 'description', 'badge_type', 'badge_goal']

class BadgeDetailSerializer(BadgeSerializer):
        def update(self, instance, validated_data):
            instance.image = validated_data.get('image',instance.image)
            instance.description = validated_data.get('description',instance.description)
            instance.badge_type = validated_data.get('badge_type',instance.badge_type)
            instance.badge_goal = validated_data.get('badge_goal',instance.badge_goal)
            instance.save()
            return instance

# /* --------------------------------------------------------- */
# /* --------------------------------------------------------- */

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    avatar = serializers.URLField()
    bio = serializers.CharField(max_length=600)
    website = serializers.URLField()
    badges = BadgeSerializer(read_only=True, many=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name', 'avatar', 'bio', 'website')
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
            last_name=validated_data['last_name'],
            avatar=validated_data['avatar'],
            bio=validated_data['bio'],
            website=validated_data['website']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class EditUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    avatar = serializers.URLField()
    bio = serializers.CharField(max_length=600)
    website = serializers.URLField()
    badges = BadgeSerializer(read_only=True, many=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class CustomUserDetailSerializer(EditUserSerializer):
        def update(self, instance, validated_data):
            instance.username = validated_data.get('username',instance.username)
            instance.email = validated_data.get('email',instance.email)
            instance.avatar = validated_data.get('avatar', instance.avatar)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.website = validated_data.get('website', instance.website)
            instance.save()
            return instance

# /* --------------------------------------------------------- */
# /* --------------------------------------------------------- */

# CREATE A USER ACCOUNT
# class RegisterSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=CustomUser.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

        
#         user.set_password(validated_data['password'])
#         user.save()

#         return user