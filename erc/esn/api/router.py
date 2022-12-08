from rest_framework import routers

from esn.api.views.esn import ObjectView

object_api_router = routers.DefaultRouter()

object_api_router.register("", ObjectView)
