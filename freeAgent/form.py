from django import forms
from .models import Member


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #TODO: optional verify password_2

    class Meta:
        model = Member
        fields = ['user_name', 'email', 'password', 'category', 'first_name', 'last_name']
