from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserLoginForm(forms.Form):

    email = forms.EmailField(max_length=150 )
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
            cleaned_data = super(UserLoginForm,self).clean()
            user = authenticate(
                email=cleaned_data['email'],
                password=cleaned_data['password'],
            )

            if user is None:
                raise forms.ValidationError(
                    'We do not see this User  ... please try again or create a new account :)'
                )
            cleaned_data['user'] = user
            return cleaned_data


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username', 'first_name',
            'last_name', 'email',
            'password1', 'password2',
        ]
