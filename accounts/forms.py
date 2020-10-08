# accounts/forms.py
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SmansaUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field

class SmansaUserCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Data User',
            'username',
            'mobile_number',
            Field('address', css_class='form-group col-md-6 mb-0'),
            'password',
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = SmansaUser
        fields = ('username', 'mobile_number', 'address', 'password')

class SmansaUserChangeForm(UserChangeForm):
    class Meta:
        model = SmansaUser
        fields = ('username', 'mobile_number', 'address')