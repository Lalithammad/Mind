from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Employee
from App.serializers import  EmployeeSerializer
# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset                 = Employee.objects.all()
    serializer_class         = EmployeeSerializer
    authentication_classes   = [ JWTAuthentication ]
    permission_classes       = [ IsAdminUser]