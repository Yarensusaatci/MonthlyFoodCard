from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import viewsets
from projects.models import Employees
from .forms import EmployeesForm
from .serializers import EmployeeSerializer

# def employee_list(request):
#      return render(request,"projects/employee_list.html")
# def employee_form(request):
#      if request.method == "GET":
#          form = EmployeesForm
#          return render(request,"projects/employee_form.html",{'form':form})
#      else:
#          if id == 0:
#              form = EmployeesForm(request.POST)
#          else:
#              employee = Employees.objects.get(pk=id)
#              form =  EmployeesForm(request.POST, instance=employee)  
#          if form.is_valid():
#              form.save()
#          return redirect('/employee/list')
# def employee_delete(request,id):
#     employee = Employees.objects.get(pk=id)
#     employee.delete()
#     return

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()
