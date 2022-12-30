from django.db import models
from contacts.models import Contacts


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.ForeignKey(
        Contacts,
        related_name="contacts_employee",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
