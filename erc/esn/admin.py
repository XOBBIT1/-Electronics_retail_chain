import asyncio
from django.contrib import admin
from esn.models import ObjectModel


async def reset_debt(modeladmin, request, queryset):
    await queryset.update(debt=0)


@admin.register(ObjectModel)
class ObjectModelAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "type", "contacts")
    list_filter = ("name", "debt", "type", "contacts")
    search_fields = ("name", "debt", "type", "contacts")
    readonly_fields = ("debt",)
    actions = [reset_debt]
