# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cliente', models.CharField(max_length=150)),
                ('Nombre', models.CharField(max_length=150)),
                ('Apellidos', models.CharField(max_length=150, null=True, blank=True)),
                ('Ci_Nit', models.PositiveIntegerField(unique=True, max_length=20)),
                ('Celular', models.PositiveIntegerField(max_length=8)),
                ('Ficha', models.PositiveIntegerField(max_length=8)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_del_Elemento', models.CharField(max_length=100)),
                ('Abreviatura', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nro_de_Lote', models.CharField(max_length=150)),
                ('Precio', models.PositiveIntegerField(max_length=8)),
                ('Cantidad', models.PositiveIntegerField(default=1, max_length=8)),
                ('Total', models.PositiveIntegerField(max_length=8)),
                ('Observaciones', models.CharField(max_length=150)),
                ('Procedencia', models.CharField(max_length=200, null=True, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('Cliente', models.ForeignKey(to='producto.Cliente')),
                ('Elemento', models.ForeignKey(to='producto.Elemento')),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Resultado', models.FloatField()),
                ('Elemento', models.CharField(max_length=100)),
                ('Abreviatura', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(to='producto.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
