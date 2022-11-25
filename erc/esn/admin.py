from django.contrib import admin
from esn.models import Factory, Distributor, Dealership, LargeRetailChain, IndividualEntrepreneur

admin.site.register([Factory, Distributor, Dealership, LargeRetailChain, IndividualEntrepreneur])
