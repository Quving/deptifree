# Create your views here.
from rest_framework import generics, permissions

from contactlist.models import ContactList
from contactlist.permissions import IsOwnerOrReadOnly
from contactlist.serializers import ContactListSerializer


class ContactListList(generics.ListCreateAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
