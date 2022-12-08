import asyncio
from django.contrib import admin
from esn.models import ObjectModel


def reset_debt(modeladmin, request, queryset):
    return queryset.update(debt=0)


class ObjectModelInline(admin.TabularInline):
    model = ObjectModel


@admin.register(ObjectModel)
class ObjectModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "debt", "type", "provider")
    list_filter = ("contacts__address__city",)
    search_fields = ("name", "debt", "type")
    inlines = [ObjectModelInline]
    actions = [reset_debt]
