# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from core.models import OneToManyDept, OneToOneDept
from core.permissions import IsOwnerOrReadOnly
from core.serializers import OneToOneDeptSerializer, OneToManyDeptSerializer
from core.serializers import UserSerializer


class OneToOneDeptList(generics.ListCreateAPIView):
    queryset = OneToOneDept.objects.all()
    serializer_class = OneToOneDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OneToOneDeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OneToOneDept.objects.all()
    serializer_class = OneToOneDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OneToManyDeptList(generics.ListCreateAPIView):
    queryset = OneToManyDept.objects.all()
    serializer_class = OneToManyDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OneToManyDeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OneToManyDept.objects.all()
    serializer_class = OneToManyDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
