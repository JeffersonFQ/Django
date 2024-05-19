from django.db import models

# Create your models here.
class Evento:
    def __init__(self, nome, tipo, valor, descricao=None, parcelas=1):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.parcelas = parcelas

salario = Evento("Salário", "Entrada", 1500, parcelas=1)
emprestimo = Evento("Empréstimo", "Saída", 1000, "Emprestimo Toninho", 15)

extratos = [
    salario,
    emprestimo,
]