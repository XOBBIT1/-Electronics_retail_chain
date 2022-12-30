from rest_framework import serializers
from contacts.models import Contacts, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["country", "city", "street", "house_number"]


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ["email", "address"]
