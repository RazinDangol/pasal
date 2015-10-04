from django.contrib import admin

# Register your models here.
from .models import Product, Category, Customer, Sales


class ProductAdmin(admin.ModelAdmin):
    fields = ('product_name', 'category', 'primary_image',
              'product_code', 'price', 'available_quantity',)
    list_display = ('product_name', 'category_link', 'product_code',
                    'price', 'available_quantity', 'created_date', 'updated_date', 'action_link')
    search_fields=['product_name',]
    def category_link(self, obj):
        category = (
            '<a href="/admin/products/category/{id}">{type}</a>'.format(id=obj.category.id, type=obj.category))
        return category
    category_link.allow_tags = True

    def action_link(self, obj):
        edit_link = ('<a href="%d">Edit</a>' % obj.id)
        delete_link = ('<a href="%d/delete">Delete</a>' % obj.id)
        return edit_link + " " + delete_link
    action_link.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_name', 'parent')
    list_display = ('category_name', 'created_date', 'updated_date', 'parent')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Sales)
