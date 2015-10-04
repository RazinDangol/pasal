from django.db import models

import os
from io import BytesIO
from PIL import Image
import re
from django.core.exceptions import ValidationError
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    product_code = models.CharField(max_length=30, unique=True)
    primary_image = models.ImageField(upload_to=os.path.join('Images','products'))
    primary_thumbnail = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available_quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
'''
    def create_thumbnail(self):
        THUMBNAIL_SIZE = (440, 330)
        if self.primary_image:
            DJANGO_TYPE = self.primary_image.file.content_type
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            IMG_EXT = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            IMG_EXT = 'png'

        image = Image.open(BytesIO(self.primary_image.read()))
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = BytesIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.primary_image.name)[-1],
                                 temp_handle.read(),
                                 content_type=DJANGO_TYPE)

        def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super().save()
'''


def number_validator(number):
    if len(str(number)) < 10:
        raise ValidationError('{} is not a valid mobile number'.format(number))
    elif not re.match('^98',str(number)):
        raise ValidationError('{} is not a valid mobile number of Nepal'.format(number))


class Customer(models.Model):
    full_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.DecimalField(
        max_digits=10, decimal_places=0, validators=[number_validator])
    profile_image = models.ImageField(
        upload_to=os.path.join('Images', 'customer'), verbose_name='Profile Picture')

    def __str__(self):
        return self.full_name


class Sales(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
    quantity = models.IntegerField()
    sales_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sales_date)
