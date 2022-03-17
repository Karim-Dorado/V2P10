from rest_framework import serializers
from .models import Comment
from users.models import User
from issues.models import Issue


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        )
    issue = serializers.SlugRelatedField(
        queryset=Issue.objects.all(),
        slug_field='title',
        )
        
    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author',
                  'issue',
                  'created_time'
                  ]