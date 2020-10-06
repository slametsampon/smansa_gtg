# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SmansaUserCreationForm, SmansaUserChangeForm
from .models import SmansaUser

@admin.register(SmansaUser)
class SmansaUserAdmin(UserAdmin):
    add_form = SmansaUserCreationForm
    form = SmansaUserChangeForm
    model = SmansaUser
    list_display = ('username','mobile_number')
    list_filter = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username',  'mobile_number')
        }),
        (None, {
            'fields': ('address',)
        }),
    )
    
