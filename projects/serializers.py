from rest_framework.serializers import ModelSerializer
from .models import Project
from rest_framework import serializers
from users.models import User
from issues.models import Issue


class ProjectSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )
    project_contributor = serializers.StringRelatedField(many=True)
    issue_related = serializers.SlugRelatedField(
        queryset=Issue.objects.all(),
        slug_field='title',
        many=True
    )
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author',
            'issue_related',
            'project_contributor',
            ]
        read_only_fields = ("author",)
    
    def create(self, validated_data):
        author = self.context['request'].user  # récupère le token

        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=author
        )
        project.save()

        return project