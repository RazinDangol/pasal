# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_customer_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('customer', models.ForeignKey(to='products.Customer')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'Sales'},
        ),
        migrations.AlterField(
            model_name='product',
            name='primary_image',
            field=models.ImageField(upload_to='Images/products'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
    ]
