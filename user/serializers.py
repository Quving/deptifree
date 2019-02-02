from rest_framework import serializers

from dept.models import Dept
from .models import ApplicationUser


class ApplicationUserSerializer(serializers.ModelSerializer):
    depts = serializers.PrimaryKeyRelatedField(many=True, queryset=Dept.objects.all())

    class Meta:
        model = ApplicationUser
        fields = ('id', 'email', 'username', 'name', 'depts')
