# accounts/forms.py
from django import forms
from django.forms import widgets, ModelForm
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

class SmansaUserCreate_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

    def clean_username(self):
        data = self.cleaned_data['username']
        
        # Remember to always return the cleaned data.
        return data

    def clean_mobile_number(self):
        data = self.cleaned_data['mobile_number']
        
        # Remember to always return the cleaned data.
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        
        # Remember to always return the cleaned data.
        return data

    def clean_bio(self):
        data = self.cleaned_data['bio']
        
        # Remember to always return the cleaned data.
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Data User',
            'username',
            'mobile_number',
            Field('address', css_class='form-group col-md-6 mb-0'),
            Field('bio', css_class='form-group col-md-6 mb-0'),
            'password',
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = SmansaUser
        fields = ('username', 'mobile_number', 'address', 'bio', 'password')

class SmansaUserChangeForm(UserChangeForm):
    class Meta:
        model = SmansaUser
        fields = ('username', 'mobile_number', 'address', 'bio')

class SmansaUserVerifyForm(ModelForm):
    CHOICES = [('1', 'Blogger'), ('2', 'Admin')]
    user_mode = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial = '1')

    def clean_user_mode(self):
        data = self.cleaned_data['user_mode']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Verify as member',
            'user_mode',
            ),
            Submit('submit', 'Verify')
        )

    class Meta:
        model = SmansaUser
        fields = ('user_mode',)

class smansauser_admin_form(forms.Form):
    pass

class SmansaUserUpdateForm(ModelForm):
    CHOICES = [('1', 'Blogger'), ('2', 'Admin')]
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    user_mode = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial = '1')

    def clean_mobile_number(self):
        data = self.cleaned_data['mobile_number']
        
        # Remember to always return the cleaned data.
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        
        # Remember to always return the cleaned data.
        return data

    def clean_bio(self):
        data = self.cleaned_data['bio']
        
        # Remember to always return the cleaned data.
        return data

    def clean_user_mode(self):
        data = self.cleaned_data['user_mode']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if self.user.is_superuser:
            self.helper.layout = Layout(
                Fieldset('Update as member',
                'mobile_number',
                Field('address', css_class='form-group col-md-6 mb-0'),
                Field('bio', css_class='form-group col-md-6 mb-0'),
                'user_mode',
                ),
                Submit('submit', 'Update')
            )
        else:
            self.helper.layout = Layout(
                Fieldset('Update as member',
                'mobile_number',
                Field('address', css_class='form-group col-md-6 mb-0'),
                Field('bio', css_class='form-group col-md-6 mb-0'),
                ),
                Submit('submit', 'Update')
            )

    class Meta:
        model = SmansaUser
        fields = ('mobile_number', 'address', 'bio', 'user_mode')
