

from rest_framework import serializers
from api.models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):      # easily move to detail page of the object.
    company_id = serializers.ReadOnlyField() # read only field
    class Meta:
        model = Company
        fields = "__all__"



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField() # read only field
    class Meta:
        model = Employee
        fields = "__all__"