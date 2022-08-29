from rest_framework import serializers
from contributors.models import Contributor
from .models import Issue
from projects.models import Project
from users.models import User
from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer


class IssueDetailSerializer(serializers.ModelSerializer):
    """
    Detail serializer of an issue model.
    """
    issue_comment = serializers.StringRelatedField(many=True)
    project = ProjectSerializer(read_only=True)
    assignee = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )
    author = UserSerializer(read_only=True)

    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'desc',
                  'tag',
                  'priority',
                  'project',
                  'status',
                  'author',
                  'assignee',
                  'created_time',
                  'issue_comment'
                  ]
        read_only_fields = ['author', 'project', 'created_time', ]

    def create(self, validated_data):
        author = self.context.get("request", None).user
        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        # check if the assignee is a contributor, else return the author as an assignee
        assignee = User.objects.get(username=self._kwargs['data']['assignee'])
        contributors = Contributor.objects.filter(project=project.pk)
        lc = []
        for cont in contributors:
            lc.append(cont.user)
        if assignee not in lc:
            assignee = self.context.get("request", None).user

        issue = Issue.objects.create(
            title=validated_data["title"],
            desc=validated_data["desc"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            project=project,
            status=validated_data["status"],
            author=author,
            assignee=assignee
        )
        issue.save()
        return issue

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class IssueSerializer(serializers.ModelSerializer):
    """
    List serializer of an issue model.
    """
    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  ]
