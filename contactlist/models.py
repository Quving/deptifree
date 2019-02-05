from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class ContactList(models.Model):
    owner = models.ForeignKey(User, related_name='contactlists', on_delete=models.CASCADE)
    contacts = models.ManyToManyField(User, related_name='contactlists_contacts')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='My favorite contacts')
