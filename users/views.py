from rest_framework import viewsets
from .models import User
from .serializers import UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = []
