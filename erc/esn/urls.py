from django.contrib import admin
from django.urls import path, include
from esn.api.router import factory_api_router, dealership_api_address_router,\
    distributor_api_address_router, lrc_api_address_router, ie_api_address_router
from esn.api.views.esn import DebtIndividualEntrepreneurView, DebtLargeRetailChainView, \
    DebtDistributorView, DebtDealershipView

urlpatterns = [
    path("_factory/", include(factory_api_router.urls)),
    path("_dealership/", include(dealership_api_address_router.urls)),
    path("_distributor/", include(distributor_api_address_router.urls)),
    path("_lrc/", include(lrc_api_address_router.urls)),
    path("-ie/", include(ie_api_address_router.urls)),
    path("debt_ie", DebtIndividualEntrepreneurView.as_view(), name="debt_ie"),
    path("debt_dealership", DebtDealershipView.as_view(), name="debt_dealership"),
    path("debt_distributor", DebtDistributorView.as_view(), name="debt_distributor"),
    path("debt_lrc", DebtLargeRetailChainView.as_view(), name="debt_lrc"),
]
