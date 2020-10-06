from django.contrib.auth.models import AbstractUser
from django.db import models


class SmansaUser(AbstractUser):

    #additional fields
    address = models.CharField(max_length=300, null=True, help_text='Enter address')
    mobile_number = models.CharField(max_length=20, null=True, help_text='Enter mobile phone number')

    #this decorator make posible to call method w/o instantiate class
    @classmethod
    #use cls instead of self
    def update_or_create_dict(cls,dtDict):

        #get first key for unique key
        k=None
        for k,v in dtDict.items():
            if k:
                break
        
        #user as unique value, kindly modify as needed
        return cls.objects.update_or_create(
            username=dtDict.get('username'),
            defaults=dtDict,
        )            

    def __str__(self):
        return self.username

