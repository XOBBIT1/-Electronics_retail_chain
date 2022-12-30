from rest_framework import serializers
from esn.models import ObjectModel
from contacts.models import Contacts


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectModel
        fields = [
            "name",
            "debt",
            "type",
            "contacts",
            "product",
            "provider",
            "employees",
            "created_at",
        ]
        read_only = ["debt"]

class ContectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = [
           "email",
        ]