from django.contrib import admin
from django.urls import path, include

# importação para usar o pillow de imagens
from django.conf import settings
from django.conf.urls.static import static

# importação das viewsets, router do rest_framework e jwt authentication
from cartaeleanor.views import IndexViewSet, IndexTextViewSet, IndexImageViewSet, IndexBackgroundViewSet, IndexPseudoImageViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router_cartaeleanor = routers.DefaultRouter()
router_cartaeleanor.register('index', IndexViewSet, basename='Index')
router_cartaeleanor.register('indextext', IndexTextViewSet, basename='IndexText')
router_cartaeleanor.register('indeximage', IndexImageViewSet, basename='IndexImage')
router_cartaeleanor.register('indexbg', IndexBackgroundViewSet, basename='IndexBg')
router_cartaeleanor.register('indexpseudoimage', IndexPseudoImageViewSet, basename='IndexPseudoImage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_cartaeleanor.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
