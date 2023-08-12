from django.contrib import admin
from django.urls import path, include
from agencia.views import DepoimentosViewSet, DepoimentosSelecionadosViewSet, DestinosViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosSelecionadosViewSet,
                basename='Depoimentos-home')
router.register('destinos', DestinosViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para add imagens por meio do gerenciador de arquivos
