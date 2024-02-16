from django.contrib import admin
from emp.models import Company,Employee

# Register your models here.


class CoampnayAdmin(admin.ModelAdmin):
    list_display = ['name']
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display =['name']
    

admin.site.register(Company,CoampnayAdmin)
admin.site.register(Employee,EmployeeAdmin)

