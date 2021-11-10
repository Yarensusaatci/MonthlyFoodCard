from django.contrib import admin
from .models import Companies, Employees, Restaurants
# Register your models here.

admin.site.register(Employees)
admin.site.register(Companies)
admin.site.register(Restaurants)