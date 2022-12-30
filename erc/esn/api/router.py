from rest_framework import routers

from esn.api.views.esn import ObjectView

delete_object_api_router = routers.DefaultRouter()

delete_object_api_router.register("", ObjectView)
