from django.contrib import admin
from esn.models import Factory, Distributor, Dealership, LargeRetailChain, IndividualEntrepreneur


async def reset_debt(modeladmin, request, queryset):
    await queryset.update(debt=0)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "employees")
    list_filter = ("name", "contacts", "created_at", "employees")
    search_fields = ("name", "contacts", "created_at", "employees")


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    list_filter = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    search_fields = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    readonly_fields = ("debt",)
    actions = [reset_debt]


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    list_filter = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    search_fields = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    readonly_fields = ("debt",)
    actions = [reset_debt]


@admin.register(LargeRetailChain)
class LargeRetailChainAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    list_filter = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    search_fields = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    actions = [reset_debt]


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    list_filter = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    search_fields = ("name", "debt", "supplier", "contacts", "created_at", "employees")
    readonly_fields = ("debt",)
    actions = [reset_debt]
