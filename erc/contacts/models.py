from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=256, null=False, blank=False)
    city = models.CharField(max_length=256, blank=False, null=False)
    street = models.CharField(max_length=256, null=True, blank=False)
    house_number = models.CharField(max_length=256, null=True, blank=False)

    class Meta:
        verbose_name = "Address"


class Contacts(models.Model):
    email = models.EmailField(
        max_length=256, unique=True, null=False, db_index=True, blank=False
    )
    address = models.ForeignKey(
        Address,
        related_name="address",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Contacts"
