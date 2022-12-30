from rest_framework import viewsets

from products.api.serializers.product import ProductSerializer
from products.models import Product


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
