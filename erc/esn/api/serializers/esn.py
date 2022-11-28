from rest_framework import serializers
from esn.models import Factory, IndividualEntrepreneur, Dealership, Distributor, LargeRetailChain


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ["name", "contacts", "product", "created_at", "employees"]


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = ["name", "contacts", "debt", "supplier", "product", "employees", "created_at"]
        read_only_fields = ('debt',)


class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ["name", "contacts", "debt", "supplier", "product", "employees", "created_at"]
        read_only_fields = ('debt',)


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ["name", "contacts", "debt", "supplier", "product", "employees", "created_at"]
        read_only_fields = ('debt',)


class LargeRetailChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = LargeRetailChain
        fields = ["name", "contacts", "debt", "supplier", "product", "employees", "created_at"]
        read_only_fields = ('debt',)
