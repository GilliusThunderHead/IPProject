from django import forms
from .models import Member
from django.contrib.auth.models import User

actor_choice = [('', 'client',), ('', 'freeAgent')]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    groups = forms.ChoiceField(widget=forms.Select, choices=actor_choice, initial=1)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def check_password(self):

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError(_('password does not match'))