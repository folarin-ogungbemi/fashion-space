from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        RestrictedList = ['ftogungbemi@gmail.com']
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact fashion space.')
        return email