from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    cliente = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    data_compra = models.DateField(auto_now_add=True)
    compra = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome.nome} - Valor = R$ {self.valor}"
