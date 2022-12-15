from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_model", "created_at")
    list_filter = ("id", "name", "product_model", "created_at")
    search_fields = ("id", "name", "product_model", "created_at")
