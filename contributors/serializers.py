from rest_framework.serializers import ModelSerializer
from .models import Contributor
from projects.models import Project
from rest_framework import serializers
from users.models import User


class ContributorSerializer(ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(),
        slug_field='title',
    )


    class Meta(object):
        model = Contributor
        fields = ('id',
                  'user',
                  'project',
                  )

    def create(self, validated_data):
        projet = Project.objects.get(pk=self.context.get("view").kwargs["project_pk"])

        contributor = Contributor.objects.create(
            user=validated_data["user"],
            project=projet
        )
        contributor.save()
        return contributor