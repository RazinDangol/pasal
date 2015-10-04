# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150919_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('category_name', models.CharField(unique=True, max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('full_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('profile_image', models.ImageField(verbose_name='Profile Picture', upload_to='Images/customer')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantity', models.IntegerField()),
                ('sales_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='products.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='primary_thumbnail',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.AddField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='products.Category', default=1),
            preserve_default=False,
        ),
    ]
