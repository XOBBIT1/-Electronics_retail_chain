from employees.models import Employees
from employees.api.serializers.employees import EmployeesSerializer
from rest_framework import viewsets


class EmployeesView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
