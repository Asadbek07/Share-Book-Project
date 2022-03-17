from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AuthUser


class CustomUserCreationForm(UserCreationForm):
    
    # add placeholder to forms data phone field and telegram
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = '@username'
        self.fields['phone_number'].widget.attrs.update({'placeholder': '97 123 45 67'})
  
    class Meta(UserCreationForm):
        model = AuthUser
        fields = UserCreationForm.Meta.fields + (
            'email',
            'phone_number',
            'avatar',
        )


