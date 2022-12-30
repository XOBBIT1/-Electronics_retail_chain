from django.urls import path, include
from employees.api.router import employees_api_router


urlpatterns = [
    path("/", include(employees_api_router.urls)),
]
