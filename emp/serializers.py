from rest_framework import serializers

from emp.models import Company,Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Company
        fields ="__all__"
    pass
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta :
        model = Employee
        fields ="__all__"
    pass