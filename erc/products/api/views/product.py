from products.api.serializers.product import ProductSerializer
from products.models import Product
from django.shortcuts import render
from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)