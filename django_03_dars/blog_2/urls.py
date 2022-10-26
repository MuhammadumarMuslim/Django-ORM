from django.urls import path 
from .views import get_employee

urlpatterns = [
    path('', get_employee, name="get-employee")
    
]
