from django.contrib.auth.models import User
from rest_framework import serializers

from .models import OneToOneDept, OneToManyDept, Dept


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ('name', 'purpose', 'value', 'field', 'paid', 'creator')


class OneToOneDeptSerializer(DeptSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = OneToOneDept
        fields = ('sender', 'receiver')


class OneToManyDeptSerializer(DeptSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = OneToManyDept
        fields = ('sender', 'receiver')


class UserSerializer(serializers.ModelSerializer):
    depts = serializers.PrimaryKeyRelatedField(many=True, queryset=Dept.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'depts')
