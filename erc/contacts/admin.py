from django.contrib import admin
from contacts.models import Contacts, Address

admin.site.register([Contacts, Address])
