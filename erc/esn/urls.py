from django.urls import path, include
# from esn.api.views.esn import DebtObjectView, AllNetObjects, ProductObjects, ObjectView
from esn.api.router import object_api_router

from .api.views.esn import ObjectView, DebtObjectView, AllNetObjects, ProductObjects, UpdateObjectView, DeleteObjectView

urlpatterns = [
    path("object/", ObjectView.as_view(), name="object"),
    path("object_debt/", DebtObjectView.as_view(), name="object_debt"),
    path("country/<str:country>/", AllNetObjects.as_view(), name="country"),
    path("product/<str:product>/", ProductObjects.as_view(), name="product"),
    path("del_object/<int:pk>", DeleteObjectView.as_view(), name="delete"),
    path("update_object/<int:pk>", UpdateObjectView.as_view(), name="delete")
]
