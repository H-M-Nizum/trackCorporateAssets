from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanyModel, EmployeeModel, DevicesModel, DevicesAssignModel, DevicesReturnedModel
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceAssignSerializer, DeviceReturnedSerializer

class CompanyViews(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

class EmployeeViews(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViews(viewsets.ModelViewSet):
    queryset = DevicesModel.objects.all()
    serializer_class = DeviceSerializer

class DeviceAssignViews(viewsets.ModelViewSet):
    queryset = DevicesAssignModel.objects.all()
    serializer_class = DeviceAssignSerializer

class DeviceReturnedViews(viewsets.ModelViewSet):
    queryset = DevicesReturnedModel.objects.all()
    serializer_class = DeviceReturnedSerializer