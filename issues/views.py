from rest_framework import viewsets
from .serializers import IssueDetailSerializer, IssueSerializer
from .permissions import IsIssueAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Issue


class IssueViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing issues instances.
    An issue should only be accessible to the author and contributors.
    Only the author of the issue can update or delete it.
    """
    serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthenticated, IsIssueAuthorOrReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action == 'list':
            return IssueSerializer
        if self.action == 'retrieve':
            return IssueDetailSerializer
        return IssueDetailSerializer
