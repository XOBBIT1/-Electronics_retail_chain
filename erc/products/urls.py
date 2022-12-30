from django.contrib import admin
from django.urls import path, include
from products.api.router import product_api_router

urlpatterns = [
    path('/', include(product_api_router.urls)),
]
