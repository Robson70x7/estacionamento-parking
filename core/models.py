from math import ceil
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=60)
    placa = models.CharField(max_length=8)
    cor = models.CharField(max_length=20)
    observacoes = models.TextField('Observações')

    def __str__(self):
        return self.modelo + ' '+ self.placa

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "Todos paramentros"

class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def hora_total(self):
        return ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.hora_total()

    def __str__(self):
        return self.veiculo.placa