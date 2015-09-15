from django.db import models

# Create your models here.


class ProductType(models.Model):
    product_type = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_type


class Product(models.Model):
    product_type = models.ForeignKey(ProductType)
    product_name = models.CharField(max_length=30)
    product_code = models.IntegerField()
    price = models.IntegerField()
    available_quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
