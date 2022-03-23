from rest_framework import serializers
from .models import Issue
from projects.models import Project
from users.models import User
from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer
from contributors.models import Contributor
from contributors.serializers import ContributorSerializer


class IssueDetailSerializer(serializers.ModelSerializer):
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
        # récupère le token
        author = self.context.get("request", None).user

        # assigne l'auteur du problème en assigné par defaut
        assignee = self.context.get("request", None).user

        # assignee = Contributor.objects.filter(user=author.pk)
        project = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])
        
        """ contributors = Contributor.objects.filter(project=project.pk)
        for contrib in contributors:
            print(contrib.user) """

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
    
    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  ]