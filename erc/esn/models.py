from django.db.models import Avg, F
from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectType(models.TextChoices):
    FACTORY = "FA", _("Factory")
    DISTRIBUTOR = "DI", _("Distributor")
    LRC = "LRC", _("Large_retail_chain")
    DECEMBER = "DE", _("December")
    IE = "IE", _("Individual_entrepreneur")


class ObjectModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, null=True)
    contacts = models.OneToOneField(
        "contacts.Contacts",
        related_name="objects_model",
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=20, choices=ObjectType.choices, default=ObjectType.FACTORY
    )
    provider = models.OneToOneField(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    product = models.ManyToManyField("products.Product", related_name="objects_model")
    employees = models.ManyToManyField(
        "employees.Employees",
        related_name="objects_model",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def calculate_average_debt():
        debt_awg = ObjectModel.objects.all().aggregate(Avg(F("debt")))
        all_data = ObjectModel.objects.all().filter(debt__gt=debt_awg["debt__avg"])
        return all_data
