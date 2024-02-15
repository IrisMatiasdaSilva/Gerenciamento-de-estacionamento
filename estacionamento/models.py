from typing import Any
from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length =  100)
    CPF  = models.CharField(max_length =  11, null = False)
    telefone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    modelo = models.CharField(max_length =  100)
    placa = models.CharField(max_length =  100, unique = True)
    cor = models.CharField(max_length =  20)
    tipo = models.CharField(max_length =  50)

    def __str__(self):
        return f" {self.clinete.nome} -  {self.modelo} - {self.tipo}"
    

class Estacionamento(models.Model):
    clienete = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    veiculos = models.ForeignKey(Veiculo, on_delete = models.CASCADE)
    horario_entrada = models.DateTimeField(auto_now_add=True)
    horario_saida = models.DateTimeField(null = True)
    valor_pagamento = models.FloatField(default=0)
    







  