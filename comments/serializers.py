from rest_framework import serializers
from .models import Comment
from issues.models import Issue
from users.serializers import UserSerializer
from issues.serializers import IssueSerializer


class CommentDetailSerializer(serializers.ModelSerializer):
    """
    Detail serializer of a comment model.
    """
    author = UserSerializer(read_only=True)

    issue = IssueSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author',
                  'issue',
                  'created_time'
                  ]

    def create(self, validated_data):
        author = self.context.get("request", None).user  # récupère le token
        issue = Issue.objects.get(pk=self.context.get("view").kwargs["issue_pk"])
        comment = Comment.objects.create(
            description=validated_data["description"],
            author=author,
            issue=issue
        )
        comment.save()
        return comment


class CommentSerializer(serializers.ModelSerializer):
    """
    List serializer of a comment model.
    """
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'author',
                  ]
