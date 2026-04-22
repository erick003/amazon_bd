# amazon/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.views import (
    VendedorViewSet, ProdutoViewSet, CategoriaViewSet, 
    ClienteViewSet, EnderecoViewSet, PedidoViewSet, ItemPedidoViewSet
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Amazon API",
      default_version='v1',
      description="Documentação da API de Pedidos",
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register(r'vendedores', VendedorViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-pedido', ItemPedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Endpoints da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]