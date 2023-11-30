from django.shortcuts import render
from rest_framework import viewsets 
from emp.models import Company,Employee
from emp.serializers import CompanySerializer,EmployeeSerializer

# Create your views here.
class ComanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer