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
    # supporter = serializers.ReadOnlyField(source='owner.id')
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class PledgeDetailSerializer(PledgeSerializer):
        def update(self, instance, validated_data):
            instance.amount = validated_data.get('amount', instance.amount)
            instance.comment = validated_data.get('comment',instance.comment)
            instance.anonymous = validated_data.get('anonymous',instance.anonymous)
            instance.supporter = validated_data.get('supporter',instance.supporter)
            instance.save()
            return instance

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    pledges = PledgeSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
    closing_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
        pledges = PledgeSerializer(many=True, read_only=True)

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description',instance.description)
            instance.goal = validated_data.get('goal', instance.goal)
            instance.image = validated_data.get('image', instance.image)
            instance.is_open = validated_data.get('is_open',instance.is_open)
            instance.date_created = validated_data.get('date_created',instance.date_created)
            instance.category = validated_data.get('category',instance.category)
            instance.owner = validated_data.get('owner',instance.owner)
            instance.save()
            return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)