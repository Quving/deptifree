from django.contrib import admin

# Register your models here.

from .models import ComplexDept, SimpleDept

admin.site.register(ComplexDept)
admin.site.register(SimpleDept)
