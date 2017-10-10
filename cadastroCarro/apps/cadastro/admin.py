# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cadastro, Carro
from django.contrib import admin


# Register your models here.
class CadastroAdmin(admin.ModelAdmin):
    model = Cadastro
    list_display = ['name', 'telefone']


admin.site.register(Cadastro, CadastroAdmin)


class CarroAdmin(admin.ModelAdmin):
    model = Carro
    list_display = ['colaborador', 'localDeOrigem', 'localDeDestino']

admin.site.register(Carro, CarroAdmin)