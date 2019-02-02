from rest_framework import serializers

from dept.models import SimpleDept, ComplexDept, Dept


class DeptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dept
        fields = ('name', 'purpose', 'value', 'field', 'paid', 'owner')


class SimpleDeptSerializer(DeptSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SimpleDept
        fields = '__all__'


class ComplexDeptSerializer(DeptSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ComplexDept
        fields = '__all__'
