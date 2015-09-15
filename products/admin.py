from django.contrib import admin

# Register your models here.
from .models import Product
from .models import ProductType
class ProductAdmin(admin.ModelAdmin):
    fields=('product_name','product_type','product_code','price','available_quantity',)
    list_display=('product_name','product_type','product_code','price','available_quantity','created_date','updated_date')
class ProductTypeAdmin(admin.ModelAdmin):
    fields=('product_type',)
    list_display=('product_type','created_date','updated_date')

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductType,ProductTypeAdmin)