from cartaeleanor.models import Index
from cartaeleanor.serializers import IndexSerializer
from rest_framework import viewsets

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer