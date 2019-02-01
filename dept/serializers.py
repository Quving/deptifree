from django.contrib.auth.models import User
from rest_framework import serializers

from dept.models import SimpleDept, ComplexDept, Dept


class DeptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dept
        fields = ('name', 'purpose', 'value', 'field', 'paid', 'creator')


class SimpleDeptSerializer(DeptSerializer):
    class Meta:
        model = SimpleDept
        fields = ('sender', 'receiver')


class ComplexDeptSerializer(DeptSerializer):
    class Meta:
        model = ComplexDept
        fields = ('sender', 'receiver')

