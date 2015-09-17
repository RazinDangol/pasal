# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150917_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='product_type',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
