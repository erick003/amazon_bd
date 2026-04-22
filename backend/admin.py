from django.contrib import admin
from .models import Cliente, Produto, Categoria, Endereco, Pedido, ItemPedido, Vendedor

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    ordering = ('nome',)

# Registre os outros modelos da mesma forma:
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Endereco)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Vendedor)
