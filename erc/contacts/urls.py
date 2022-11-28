from django.contrib import admin
from django.urls import path, include
from contacts.api.router import contacts_api_router, contacts_api_address_router

urlpatterns = [
    path("/", include(contacts_api_router.urls)),
    path("_address/", include(contacts_api_address_router.urls)),
]
