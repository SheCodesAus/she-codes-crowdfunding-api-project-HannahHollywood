from email.mime import image
from unicodedata import category
from rest_framework import serializers
from .models import Project, Pledge, Category

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    project_goal = serializers.IntegerField()
    project_image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    # pledges = PledgeSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
        pledges = PledgeSerializer(many=True, read_only=True)

        def update(self, instance, validated_data):
            instance.project_title = validated_data.get('project_title', instance.project_title)
            instance.description = validated_data.get('description',instance.description)
            instance.project_goal = validated_data.get('project_goal', instance.project_goal)
            instance.project_image = validated_data.get('project_image', instance.project_image)
            instance.is_open = validated_data.get('is_open',instance.is_open)
            instance.date_created = validated_data.get('date_created',instance.date_created)
            instance.category = validated_data.get('category',instance.category)
            instance.owner = validated_data.get('owner', instance.owner)
            instance.save()
            return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)