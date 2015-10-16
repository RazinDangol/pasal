# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20151015_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=20, default=123),
            preserve_default=False,
        ),
    ]
