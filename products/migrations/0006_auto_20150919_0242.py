# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150917_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='primary_image',
            field=models.ImageField(default=12, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
