from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)

urlpatterns=[
     # path('',views.employee_form),
     # path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
     # path('list/',views.employee_list,name='employee_list'),
     path('',include(router.urls))
    ]