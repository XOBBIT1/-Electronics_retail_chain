from rest_framework import routers
from contacts.api.views.contacts import ContactsView, AddressView

contacts_api_router = routers.DefaultRouter()

contacts_api_router.register("", ContactsView)

contacts_api_address_router = routers.SimpleRouter()

contacts_api_address_router.register("", AddressView)
