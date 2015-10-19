# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20151016_0600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
