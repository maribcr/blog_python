# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('horario', models.DateTimeField(auto_now_add=True)),
                ('localDeOrigem', models.CharField(blank=True, max_length=255, verbose_name='Local de Origem')),
                ('localDeDestino', models.CharField(blank=True, max_length=255, verbose_name='Local de Destino')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Pedido de Carro',
                'verbose_name_plural': 'Pedidos de Carros',
            },
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='data',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='localDeDestino',
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='localDeOrigem',
        ),
        migrations.AddField(
            model_name='carro',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cadastro'),
        ),
    ]
