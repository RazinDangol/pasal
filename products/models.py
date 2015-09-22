from django.db import models

# Create your models here.


class ProductType(models.Model):
    product_type = models.CharField(max_length=30,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_type


class Product(models.Model):
    product_type = models.ForeignKey(ProductType)
    product_name = models.CharField(max_length=30)
    product_code = models.CharField(max_length=30,unique=True)
    primary_image= models.ImageField(upload_to='Images')
    price = models.DecimalField(max_digits=9,decimal_places=2)
    available_quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
