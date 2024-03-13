from django.db import models

# Create your models here.

# Create database model for Company 
class CompanyModel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    since_year = models.IntegerField()

    def __str__(self):
        return self.name

# Create database model for Employee
class EmployeeModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    joining_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.company}"

# Create database model for Devices
class DevicesModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.company}"

# Create database model for Devices Assign
class DevicesAssignModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    divice = models.ForeignKey(DevicesModel, on_delete=models.CASCADE)
    assign_time = models.DateTimeField()
    returned_deadeline = models.DateTimeField()
    device_condition = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.divice}"

# Create database model for Devices Returned
class DevicesReturnedModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    divice = models.ForeignKey(DevicesModel, on_delete=models.CASCADE)
    returned_time = models.DateTimeField()
    device_condition = models.TextField()
    isConditionSatisfy = models.BooleanField()

    def __str__(self):
        return f"{self.employee} - {self.divice}"
    