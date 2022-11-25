from django.db import models
from contacts.models import Contacts


class Factory(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    contacts = models.ForeignKey(
        Contacts,
        related_name="contacts_factory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ManyToManyField(
        "products.Product", related_name="product_factory", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    employees = models.CharField(max_length=256, null=False, blank=False)


class Distributor(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    contacts = models.ForeignKey(
        Contacts,
        related_name="contacts_distributor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    supplier = models.ForeignKey(
        Factory,
        related_name="supplier_distributor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ManyToManyField(
        "products.Product", related_name="product_distributor", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    employees = models.CharField(max_length=256, null=False, blank=False)


class Dealership(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    contacts = models.ForeignKey(
        Contacts,
        related_name="contacts_dealership",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    supplier = models.ForeignKey(
        Distributor,
        related_name="supplier_dealership",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ManyToManyField(
        "products.Product", related_name="product_dealership", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    employees = models.CharField(max_length=256, null=False, blank=False)


class LargeRetailChain(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    contacts = models.ForeignKey(
        Contacts,
        related_name="contacts_lrc",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    supplier = models.ForeignKey(
        Dealership,
        related_name="supplier_lrc",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ManyToManyField(
        "products.Product", related_name="product_lrc", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    employees = models.CharField(max_length=256, null=False, blank=False)


class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    contacts = models.ForeignKey(
        Contacts,
        related_name="contacts_ie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    product = models.ManyToManyField(
        "products.Product", related_name="product_ie", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(
        LargeRetailChain,
        related_name="supplier_ie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    employees = models.CharField(max_length=256, null=False, blank=False)
