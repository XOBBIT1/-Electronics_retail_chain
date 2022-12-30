from rest_framework import routers
from employees.api.views.employees import EmployeesView

employees_api_router = routers.DefaultRouter()

employees_api_router.register("", EmployeesView)
