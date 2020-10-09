# blog/forms.py
from django import forms
from django.forms import widgets, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Blog, BlogComment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field


class BlogCreate_form(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':12}))

    def clean_title(self):
        data = self.cleaned_data['title']
        
        # Remember to always return the cleaned data.
        return data

    def clean_description(self):
        data = self.cleaned_data['description']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Blog',
            Field('title', css_class='form-group col-md-4 mb-0'),
            Field('description', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Blog
        fields = ('title', 'description',)

class BlogCommentCreate_form(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    def clean_description(self):
        data = self.cleaned_data['description']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Comment',
            Field('description', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = BlogComment
        fields = ('description',)
