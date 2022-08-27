from rest_framework import viewsets
from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer
from .permissions import IsCommentAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet, IsCommentAuthorOrReadOnly):
    """
    A viewset for viewing and editing comments instances.
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentSerializer
        if self.action == 'retrieve':
            return CommentDetailSerializer
        return CommentDetailSerializer
