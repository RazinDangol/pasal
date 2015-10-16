# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20151008_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, verbose_name='Profile Picture', upload_to='Images/customer'),
        ),
    ]
