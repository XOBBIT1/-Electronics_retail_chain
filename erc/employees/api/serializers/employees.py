from rest_framework import serializers
from employees.models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ["name", "address",  "created_at"]
