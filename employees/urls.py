from django.urls import path
from employees import views


urlpatterns = [
    path('employee_details/<int:pk>', views.employee_detail, 
         name='employee-details'),
]