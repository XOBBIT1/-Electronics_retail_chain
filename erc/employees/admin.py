from django.contrib import admin
from employees.models import Employees


# Register your models here.
@admin.register(Employees)
class ObjectModelAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "created_at")
    list_filter = ("name", "address", "created_at")
    search_fields = ("name", "address", "created_at")
