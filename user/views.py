# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics

from . import serializers

User = get_user_model()


class ApplicationUserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ApplicationUserSerializer


class ApplicationUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ApplicationUserSerializer
