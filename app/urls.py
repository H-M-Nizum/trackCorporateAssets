from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViews, EmployeeViews, DeviceViews, DeviceAssignViews, DeviceReturnedViews

router = DefaultRouter()
router.register(r'companies', CompanyViews)
router.register(r'employees', EmployeeViews)
router.register(r'devices', DeviceViews)
router.register(r'assign', DeviceAssignViews)
router.register(r'returned', DeviceReturnedViews)

urlpatterns = [
    path('', include(router.urls)),
]
