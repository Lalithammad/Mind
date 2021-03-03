from django.db.models.fields import CharField, DateField, EmailField, IntegerField
from rest_framework import fields, serializers
from App.models import Employee

def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')

class EmployeeSerializer(serializers.ModelSerializer):
    email        = serializers.EmailField(required=True)
    firstname    = serializers.CharField(required=True)
    password     = serializers.CharField(required=True)
    mobile       = serializers.IntegerField(required=True)
    dob          = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y',],required=True)
    
    class Meta:
        model  = Employee
        fields = '__all__'
        