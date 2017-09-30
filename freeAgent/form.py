from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField

actor_choice = [('', 'client',), ('', 'freeAgent')]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    # groups = forms.ChoiceField(widget=forms.Select, choices=actor_choice)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def clean_password2(self):

        """
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("not match")
        return cd['password2']
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise ValidationError("password does not match")


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput()
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))
