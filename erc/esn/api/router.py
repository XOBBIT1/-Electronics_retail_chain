from rest_framework import routers
from esn.api.views.esn import FactoryView, DistributorView, DealershipView, IndividualEntrepreneurView,\
    LargeRetailChainView, DebtIndividualEntrepreneurView

factory_api_router = routers.DefaultRouter()

factory_api_router.register("", FactoryView)

distributor_api_address_router = routers.SimpleRouter()

distributor_api_address_router.register("", DistributorView)

dealership_api_address_router = routers.SimpleRouter()

dealership_api_address_router.register("", DealershipView)

ie_api_address_router = routers.SimpleRouter()

ie_api_address_router.register("", IndividualEntrepreneurView)

lrc_api_address_router = routers.SimpleRouter()

lrc_api_address_router.register("", LargeRetailChainView)
