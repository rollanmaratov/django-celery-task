from django.db import models
from organization.service import send


class Institution(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    # employee has supervisor
    supervisor = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.surname + " " + self.first_name + " " + self.patronymic_name


class Department(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    upper_level = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.employee.surname + ' ' + self.employee.first_name + ' ' + self.employee.patronymic_name


class Task(models.Model):
    task = models.TextField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.employee.first_name + ': ' + self.task
