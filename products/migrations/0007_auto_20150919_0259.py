# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150919_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='primary_image',
            field=models.ImageField(upload_to='Images'),
        ),
    ]
