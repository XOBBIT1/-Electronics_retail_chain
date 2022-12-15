from django.contrib import admin
from contacts.models import Contacts, Address


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "address")
    list_filter = ("email", "address")
    search_fields = ("email", "address")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street", "house_number")
    list_filter = ("country", "city", "street", "house_number")
    search_fields = ("country", "city", "street", "house_number")
