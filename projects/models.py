from django.db import models
from django.db.models.base import Model
from datetime import datetime

from django.db.models.deletion import CASCADE
# from rest_framework import serializers

EMPLOYEE_BUDGET_TYPE = [
('300', 'smallTown'),
('500', 'cityCenter'),
]

CARD_TYPE = [
('1', 'active'),
('2', 'terminated'),
]
class Employees(models.Model):
    empName = models.CharField(max_length=100)
    empSurname = models.CharField(max_length=100)
    compName =   models.CharField(max_length=100)
    # compName =   models.ForeignKey(Companies, default=1, on_delete=models.CASCADE, db_column = 'companies')
    budgetStatus = models.CharField(max_length=10, choices=EMPLOYEE_BUDGET_TYPE) # 1 is for $300, 2 is for $500  
    active = models.CharField(max_length=10, choices=CARD_TYPE, default=1) # is activated
    # active = models.BooleanField(default=True)
    balance = models.IntegerField()
    date = models.DateTimeField(default=datetime.now ,blank=True) #?

    def __str__(self):
        return self.empName

    class Meta:
        db_table = "employees"
        ordering = ['empName']
     

class Restaurants(models.Model):
    resName = models.CharField(max_length=100)
    resAccount =  models.IntegerField()
    
    def __str__(self):
        return self.resName
    
    class Meta:
        db_table = "restaurants"
        ordering = ['resName']

class Companies(models.Model):
    compName = models.CharField(max_length=100)
    compAccount = models.IntegerField()
    employees = models.ManyToManyField(Employees, blank=True, related_name='employees')
    restaurants = models.ManyToManyField(Restaurants, blank=True, related_name='restaurants') 
    #memberRestaurantsList = serializers.ListField(child=serializers.models.IntegerField())
    date = models.DateTimeField(default=datetime.now ,blank=True) #?
    
    def __str__(self):
        return self.compName

    class Meta:
        db_table = "companies"
        ordering = ['compName']

    