# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ApplicationUserCreationForm, ApplicationUserChangeForm
from .models import ApplicationUser


class ApplicationUserAdmin(UserAdmin):
    add_form = ApplicationUserCreationForm
    form = ApplicationUserChangeForm
    model = ApplicationUser
    list_display = ['email', 'username', 'name']


admin.site.register(ApplicationUser, ApplicationUserAdmin)
