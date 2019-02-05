from rest_framework import serializers

from contactlist.models import ContactList


class ContactListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ContactList
        fields = ('name', 'contacts', 'owner')
