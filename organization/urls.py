from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.EmployeeAPIView.as_view()),
    path('employees/<int:id>', views.EmployeeDetails.as_view()),
    path('positions/', views.PositionAPIView.as_view()),
    path('positions/<int:id>', views.PositionDetails.as_view()),
    path('departments/', views.DepartmentAPIView.as_view()),
    path('departments/<int:id>', views.DepartmentDetails.as_view()),
    path('institutions/', views.InstitutionAPIView.as_view()),
    path('institutions/<int:id>', views.InstitutionDetails.as_view()),
    path('tasks/', views.TaskAPIView.as_view()),
    path('tasks/<int:id>', views.TaskDetails.as_view()),
]