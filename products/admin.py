from django.contrib import admin

# Register your models here.
from .models import Product
from .models import ProductType


class ProductAdmin(admin.ModelAdmin):
    fields = ('product_name', 'product_type',
              'product_code', 'price', 'available_quantity',)
    list_display = ('product_name', 'product_type', 'product_code',
                    'price', 'available_quantity', 'created_date', 'updated_date','action_link')

    def action_link(self,obj):
        edit_link=('<a href="%d">Edit</a>' % obj.id)
        delete_link=('<a href="delete/%d">Delete</a>'  % obj.id)
        return edit_link + " " + delete_link
    action_link.allow_tags=True


class ProductTypeAdmin(admin.ModelAdmin):
    fields = ('product_type',)
    list_display = ('product_type', 'created_date', 'updated_date')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
