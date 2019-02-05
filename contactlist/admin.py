# Register your models here.
from django.contrib.admin import site

from contactlist.models import ContactList

site.register(ContactList)
