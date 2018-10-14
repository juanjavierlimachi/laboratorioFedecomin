# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20181008_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Ficha',
        ),
    ]
