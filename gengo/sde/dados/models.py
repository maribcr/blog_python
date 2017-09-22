from django.db import models
from django.utils import timezone
import datetime
from bakery.models import BuildableModel


class PublicoGeral(models.Model):
    ano = models.IntegerField(default=None, null=True, blank=True)
    media_pagante = models.Model(default=None, null=True, blank=True)
    pct_ocupacao = models.IntegerField(default=None, null=True, blank=True)


class ScoutTipo(models.Model):
    descricao_plural = models.CharField(max_length=60, null=True)
    nome = models.CharField(max_length=60, null=True)
    scout_tipo_id = models.IntegerField(default=None, null=True)
    descricao = models.CharField(max_length=60, null=True)
    sigla = models.CharField(max_length=3, null=True)


class Equipe(models.Model):
    #informações
    equipe_id = models.IntegerField(default=0)
    nome_popular = models.CharField(max_length=30)
    nome = models.CharField(max_length=60, null=True)
    organizacao_id = models.IntegerField(default=0, null=True)
    slug = models.CharField(max_length=60, null=True)
    sigla = models.CharField(max_length=3, null=True)

    #escudos
    escudo_gd = models.CharField(max_length=200, null=True)
    escudo_md = models.CharField(max_length=200, null=True)
    escudo_pq = models.CharField(max_length=200, null=True)

    #cores
    cor_1 = models.CharField(max_length=7, null=True)
    cor_2 = models.CharField(max_length=7, null=True)
    cor_3 = models.CharField(max_length=7, null=True)

    #é Publicável?
    publicavel = models.NullBooleanField(null=True, blank=True)

    #tem dados completos
    integra = models.NullBooleanField(null=True, blank=True)
    ranking_abc = models.IntegerField(default=None, null=True, blank=True)
    css = models.CharField(max_length=120, null=True, blank=True)

    #é o modelo certo
    nacion = models.NullBooleanField(null=True, blank=True)

    def __unicode__(self):
        return self.nome_popular

    def get_absolute_url(self):
        return r'^futebol/publico-no-brasil/time/'+str(self.slug)+'/'

class Campeonato(models.Model):
    campeonato_slug = models.SlugField(max_length=50)
    edicao_slug = models.SlugField(max_length=50)
    ano = models.SmallIntegerField()
    nome = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, null=True, blank=True)
    publicavel = models.NullBooleanField(null=True, blank=True)
    cor = models.CharField(max_length=7, null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True)
    integra = models.NullBooleanField(null=True, blank=True)