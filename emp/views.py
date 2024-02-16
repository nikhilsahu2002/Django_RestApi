from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets 
from emp.models import Company,Employee
from emp.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response
# Create your views here.
class ComanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # company/{compnay_id}/employee
    @action(detail=True,methods=['get'])
    def employee(self,req,pk):
       try:
            company =Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company = company)
            empsrilizer = EmployeeSerializer(emps,many =True,context ={'request':req})
            return Response(empsrilizer.data)
       except Exception as e:
           return Response({'message':'error the dataset is empty'})
           

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer()