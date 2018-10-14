# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_remove_cliente_ficha'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Ficha',
            field=models.PositiveIntegerField(default='9', max_length=8),
            preserve_default=False,
        ),
    ]
