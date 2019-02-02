from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Dept(models.Model):
    owner = models.ForeignKey(User, related_name='depts', on_delete=models.CASCADE, default=0)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,
                            blank=True,
                            default='')
    purpose = models.TextField(max_length=100,
                               blank=True,
                               default='')
    value = models.FloatField(default=0)
    paid = models.BooleanField(default=False)


class ComplexDept(Dept):
    sender = models.ManyToManyField(User)
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='%(class)s_receiver')

    class Meta:
        ordering = ('created',)


class SimpleDept(Dept):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='%(class)s_receiver')

    class Meta:
        ordering = ('created',)
