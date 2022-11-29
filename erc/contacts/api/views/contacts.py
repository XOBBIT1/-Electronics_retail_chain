from contacts.models import Contacts, Address
from contacts.api.serializers.contacts import ContactsSerializer, AddressSerializer
from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
