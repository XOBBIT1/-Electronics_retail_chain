from rest_framework import routers
from products.api.views.product import ProductView

product_api_router = routers.DefaultRouter()

product_api_router.register("contact", ProductView)


