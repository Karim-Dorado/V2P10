from rest_framework import viewsets
from .models import Contributor
from .serializers import ContributorSerializer, ContributorDetailSerializer
from rest_framework.permissions import IsAuthenticated


class ContributorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing contributors instances.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action == 'list':
            return ContributorSerializer
        if self.action == 'retrieve':
            return ContributorDetailSerializer
        return ContributorDetailSerializer
