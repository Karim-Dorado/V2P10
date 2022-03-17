from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from contributors.models import Contributor
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.
# Seuls les contributeurs sont autorisés à créer ou à consulter les problèmes
# d'un projet.


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)

        return (Project.objects.filter(author=self.request.user)
                | Project.objects.filter(project_contributor__in=contributors)).distinct()
