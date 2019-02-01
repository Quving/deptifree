# Create your views here.
from rest_framework import generics

from . import models
from . import serializers

class ApplicationUserListView(generics.ListCreateAPIView):
    queryset = models.ApplicationUser.objects.all()
    serializer_class = serializers.ApplicationUserSerializer


class ApplicationUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ApplicationUser.objects.all()
    serializer_class = serializers.ApplicationUserSerializer
