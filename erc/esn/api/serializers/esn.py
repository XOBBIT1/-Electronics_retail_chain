from rest_framework import serializers
from esn.models import ObjectModel


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
