from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Dept(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,
                            blank=True,
                            default='')
    purpose = models.TextField(max_length=100,
                               blank=True,
                               default='')
    value = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    creator = models.ForeignKey(User,
                                related_name='%(class)s_creator',
                                on_delete=models.CASCADE, )


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
