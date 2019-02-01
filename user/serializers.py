from rest_framework import serializers

from .models import ApplicationUser


class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = ('email', 'username','name')
