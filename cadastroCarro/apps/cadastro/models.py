# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

now = timezone.now()


class Cadastro(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nome')
    telefone = models.CharField(max_length=50, blank=True)
    cep = models.CharField(max_length=8, unique=True, verbose_name='CEP')
    logadouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"


class Carro(models.Model):
    colaborador = models.ForeignKey(Cadastro)
    data = models.DateTimeField(null=True, blank=True, verbose_name='Data')
    horario = models.DateTimeField(auto_now_add=True)
    localDeOrigem = models.CharField(max_length=255, blank=True, verbose_name='Local de Origem')
    localDeDestino = models.CharField(max_length=255, blank=True, verbose_name='Local de Destino')
    descricao = models.TextField(max_length=500, verbose_name='Descrição')

    def __unicode__(self):
        return self.colaborador

    class Meta:
        verbose_name = "Pedido de Carro"
        verbose_name_plural = "Pedidos de Carros"
