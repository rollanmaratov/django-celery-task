from django.http import HttpResponse
from .tasks import send_notification
from .models import Employee, Institution, Department, Position, Task
from .serializers import EmployeeSerializer, InstitutionSerializer, DepartmentSerializer, PositionSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView

# Сотрудники


class EmployeeAPIView(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Департаменты


class DepartmentAPIView(APIView):

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetails(APIView):

    def get_object(self, id):
        try:
            return Department.objects.get(id=id)

        except Department.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        department = self.get_object(id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, id):
        department = self.get_object(id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        department = self.get_object(id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Позиции

class PositionAPIView(APIView):

    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionDetails(APIView):

    def get_object(self, id):
        try:
            return Position.objects.get(id=id)

        except Position.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        position = self.get_object(id)
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def put(self, request, id):
        position = self.get_object(id)
        serializer = PositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        position = self.get_object(id)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Организации


class InstitutionAPIView(APIView):

    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstitutionDetails(APIView):

    def get_object(self, id):
        try:
            return Institution.objects.get(id=id)

        except Institution.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        institution = self.get_object(id)
        serializer = InstitutionSerializer(institution)
        return Response(serializer.data)

    def put(self, request, id):
        institution = self.get_object(id)
        serializer = InstitutionSerializer(institution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        institution = self.get_object(id)
        institution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Задания сотрудников


class TaskAPIView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # После создания задания, оно отправится на почту сотрудника в указанное время UTC+0
            employee_id = int(request.data.get('employee'))
            task_description = request.data.get('task')
            deadline = request.data.get('deadline')
            employee = Employee.objects.get(id__exact=employee_id)
            send_notification.apply_async(
                (employee.email, employee.first_name, task_description), eta=deadline)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):

    def get_object(self, id):
        try:
            return Task.objects.get(id=id)

        except Task.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
