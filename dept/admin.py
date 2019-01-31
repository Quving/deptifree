from django.contrib import admin

# Register your models here.

from .models import OneToManyDept, OneToOneDept

admin.site.register(OneToManyDept)
admin.site.register(OneToOneDept)
