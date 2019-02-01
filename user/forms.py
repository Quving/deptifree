from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ApplicationUser


class ApplicationUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ApplicationUser
        fields = ('username', 'email', 'name')


class ApplicationUserChangeForm(UserChangeForm):
    class Meta:
        model = ApplicationUser
        fields = UserChangeForm.Meta.fields
