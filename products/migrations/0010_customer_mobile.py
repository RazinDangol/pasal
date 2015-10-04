# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20151004_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.DecimalField(default=1234567890, decimal_places=0, max_digits=10, validators=[products.models.number_validator]),
            preserve_default=False,
        ),
    ]
