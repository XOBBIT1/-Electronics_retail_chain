from rest_framework import serializers
from esn.models import ObjectModel


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectModel
        fields = ["name", "debt", "type", "contacts", "product", "employees", "created_at"]

