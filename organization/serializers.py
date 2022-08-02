# from python to json
from rest_framework import serializers
from .models import Employee, Institution, Position, Department, Task


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id', 'name', 'city', 'address']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'institution', 'upper_level']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title', 'employee', 'department']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task', 'employee', 'deadline']


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer(
        read_only=True, many=True, source="position_set")

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'surname', 'patronymic_name', 'position',
                  'date_of_birth', 'phone', 'home_address', 'email', 'supervisor']
