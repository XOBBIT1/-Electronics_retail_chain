from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "product_model", "created_at")
    list_filter = ("name", "product_model", "created_at")
    search_fields = ("name", "product_model", "created_at")
