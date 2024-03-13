from rest_framework import serializers
from .models import CompanyModel, EmployeeModel, DevicesModel, DevicesAssignModel, DevicesReturnedModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesModel
        fields = '__all__'

class DeviceAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesAssignModel
        fields = '__all__'

class DeviceReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicesReturnedModel
        fields = '__all__'