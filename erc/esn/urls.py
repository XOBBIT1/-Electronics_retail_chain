from django.urls import path, include

from .api.views.esn import (
    ObjectView,
    DebtObjectView,
    AllNetObjects,
    ProductObjects,
    UpdateObjectView,
    DeleteObjectView,
    SendEmailView,
    GetAllContactsView,
    ObjectPostView,
)

urlpatterns = [
    path("object/", ObjectView.as_view(), name="object"),
    path("object_create/", ObjectPostView.as_view(), name="create"),
    path("object_debt/", DebtObjectView.as_view(), name="object_debt"),
    path("country/<str:country>/", AllNetObjects.as_view(), name="country"),
    path("product/<str:product>/", ProductObjects.as_view(), name="product"),
    path("del_object/<int:pk>", DeleteObjectView.as_view(), name="delete"),
    path("update_object/<int:pk>", UpdateObjectView.as_view(), name="update"),
    path("send_email/", SendEmailView.as_view(), name="send"),
    path("contacts/", GetAllContactsView.as_view(), name="contacts"),
]
