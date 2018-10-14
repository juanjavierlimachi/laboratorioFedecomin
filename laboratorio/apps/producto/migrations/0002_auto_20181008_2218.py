# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Celular',
            field=models.PositiveIntegerField(max_length=8, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Ci_Nit',
            field=models.PositiveIntegerField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
