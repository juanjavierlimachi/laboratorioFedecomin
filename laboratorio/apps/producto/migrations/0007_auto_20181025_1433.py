# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_auto_20181025_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='Detalle',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
