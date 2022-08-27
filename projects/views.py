from rest_framework import viewsets
from .models import Project
from .serializers import ProjectDetailSerializer, ProjectSerializer
from contributors.models import Contributor
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    A project should only be accessible to the author and contributors.
    """
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)

        return (Project.objects.filter(author=self.request.user)
                | Project.objects.filter(project_contributor__in=contributors)).distinct()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectSerializer
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectDetailSerializer
