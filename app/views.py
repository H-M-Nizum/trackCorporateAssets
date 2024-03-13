from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanyModel, EmployeeModel, DevicesModel, DevicesAssignModel, DevicesReturnedModel
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceAssignSerializer, DeviceReturnedSerializer

class CompanyViews(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class EmployeeViews(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class DeviceViews(viewsets.ModelViewSet):
    queryset = DevicesModel.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class DeviceAssignViews(viewsets.ModelViewSet):
    queryset = DevicesAssignModel.objects.all()
    serializer_class = DeviceAssignSerializer

class DeviceReturnedViews(viewsets.ModelViewSet):
    queryset = DevicesReturnedModel.objects.all()
    serializer_class = DeviceReturnedSerializer