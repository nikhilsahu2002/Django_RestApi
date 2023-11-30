from django.contrib import admin
from django.urls import include, path
from emp.views import ComanyViewSet,EmployeeViewSet
from rest_framework import routers


Router = routers.DefaultRouter()
Router.register(r'Companies',ComanyViewSet)
Router.register(r'Employee',EmployeeViewSet)

urlpatterns = [

    path('',include(Router.urls))
]