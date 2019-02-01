# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from dept.models import ComplexDept, SimpleDept
from dept.permissions import IsOwnerOrReadOnly
from dept.serializers import SimpleDeptSerializer, ComplexDeptSerializer

User = get_user_model()


class SimpleDeptList(generics.ListCreateAPIView):
    queryset = SimpleDept.objects.all()
    serializer_class = SimpleDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SimpleDeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SimpleDept.objects.all()
    serializer_class = SimpleDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class ComplexDeptList(generics.ListCreateAPIView):
    queryset = ComplexDept.objects.all()
    serializer_class = ComplexDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ComplexDeptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComplexDept.objects.all()
    serializer_class = ComplexDeptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
