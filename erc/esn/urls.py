from django.urls import path, include
from esn.api.router import object_api_router
from esn.api.views.esn import DebtObjectView, AllNetObjects


urlpatterns = [
    path("object/", include(object_api_router.urls)),
    path("object_debt/", DebtObjectView.as_view(), name="object"),
    path("<str:country>", AllNetObjects.as_view(), name="country"),
]
