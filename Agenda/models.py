from django.db import models

# Define a tabela de tipo
class Tipo(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    # Define o nome no painel de admin
    def __str__(self):
        return f"{self.nome}[{self.id}]"

# define a tbela de eventos
class Evento(models.Model):
    nome = models.CharField(max_length=20)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=250)
    parcela = models.IntegerField(blank=True) 
    status = models.CharField(max_length=20)