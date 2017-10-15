from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import CardSerializer
from .models import Card


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)

