from rest_framework import viewsets
from .models import Contributor
from .serializers import ContributorSerializer
from rest_framework.permissions import IsAuthenticated

class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Contributor.objects.all()