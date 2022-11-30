import asyncio
from django.contrib import admin
from esn.models import ObjectModel


def reset_debt(modeladmin, request, queryset):
    return queryset.update(debt=0)


@admin.register(ObjectModel)
class ObjectModelAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "type")
    list_filter = ("name", "debt", "type")
    search_fields = ("name", "debt", "type")
    readonly_fields = ("debt",)
    actions = [reset_debt]
