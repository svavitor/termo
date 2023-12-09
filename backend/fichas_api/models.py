from django.db import models

class Ficha(models.Model):
    cpf_cnpj = models.BigIntegerField(default=False)
    nome = models.CharField(max_length=255)
    identidade = models.BigIntegerField(default=False)
    profissao = models.CharField(max_length=200)
    naturalidade = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=255)
    endereco = models.TextField(max_length=500) #Temporario
