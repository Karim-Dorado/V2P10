from rest_framework import serializers
from .models import Project
from contributors.models import Contributor
from users.serializers import UserSerializer


class ProjectDetailSerializer(serializers.ModelSerializer):
    """
    Detail serializer of a project model.
    """
    project_contributor = serializers.StringRelatedField(many=True)
    issue_related = serializers.StringRelatedField(many=True)
    author = UserSerializer(read_only=True)

    class Meta:

        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'author',
                  'issue_related',
                  'project_contributor',
                  ]
        read_only_fields = ("author",)

    def create(self, validated_data):
        author = self.context.get("request", None).user

        project = Project.objects.create(
            title=validated_data["title"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=author
        )

        new_contributor = Contributor(
                user=author,
                project=Project.objects.last(),
                permission='author',
                role='author',
            )
        new_contributor.save()

        project.save()

        return project


class ProjectSerializer(serializers.ModelSerializer):
    """
    List serializer of a project model.
    """
    class Meta:

        model = Project
        fields = ['id',
                  'title',
                  ]
