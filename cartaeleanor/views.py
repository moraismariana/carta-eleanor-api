from cartaeleanor.models import Index, IndexText, IndexImage, IndexBackground, IndexPseudoImage
from cartaeleanor.serializers import IndexSerializer, IndexTextSerializer, IndexImageSerializer, IndexBackgroundSerializer, IndexPseudoImageSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PermissaoCartaEleanor(permissions.BasePermission):
    """
    Permissão personalizada para verificar se o usuário faz parte do grupo de editores.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Verifica se o usuário está no grupo 'Editores Carta Eleanor'
        return request.user.groups.filter(name='Editores Carta Eleanor').exists()

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoCartaEleanor]

class IndexTextViewSet(viewsets.ModelViewSet):
    queryset = IndexText.objects.all()
    serializer_class = IndexTextSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoCartaEleanor]

class IndexImageViewSet(viewsets.ModelViewSet):
    queryset = IndexImage.objects.all()
    serializer_class = IndexImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoCartaEleanor]

class IndexBackgroundViewSet(viewsets.ModelViewSet):
    queryset = IndexBackground.objects.all()
    serializer_class = IndexBackgroundSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoCartaEleanor]

class IndexPseudoImageViewSet(viewsets.ModelViewSet):
    queryset = IndexPseudoImage.objects.all()
    serializer_class = IndexPseudoImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoCartaEleanor]