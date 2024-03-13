from django.contrib import admin
from .models import CompanyModel, EmployeeModel, DevicesModel, DevicesAssignModel, DevicesReturnedModel
# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(EmployeeModel)
admin.site.register(DevicesModel)
admin.site.register(DevicesAssignModel)
admin.site.register(DevicesReturnedModel)
