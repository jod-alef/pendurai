from django.db import models


# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereço = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    nome = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.FloatField()
    valor = models.FloatField()

    def __str__(self):
        return f"{self.nome.nome} - Débito = R$ {self.valor}"
