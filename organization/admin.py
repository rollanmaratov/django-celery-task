from django.contrib import admin
from .models import Employee, Institution, Department, Position, Task

admin.site.register(Employee)
admin.site.register(Institution)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Task)