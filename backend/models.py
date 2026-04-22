from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'categorias'

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    class Meta:
        db_table = 'produtos'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clientes'

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  
    cep = models.CharField(max_length=9)

    class Meta:
        db_table = 'enderecos'

class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50) # Ex: Pendente, Enviado, Entregue
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pedidos'

class ItemPedido(models.Model):
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'itens_pedido'