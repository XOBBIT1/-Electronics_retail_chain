import asyncio
from django.contrib import admin
from esn.models import ObjectModel
from .tasks import reset_debt_task

def reset_debt(modeladmin, request, queryset):
    return reset_debt_task(queryset)


class ObjectModelInline(admin.TabularInline):
    model = ObjectModel


@admin.register(ObjectModel)
class ObjectModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "debt", "type", "provider")
    list_filter = ("contacts__address__city",)
    search_fields = ("name", "debt", "type")
    inlines = [ObjectModelInline]
    actions = [reset_debt]
