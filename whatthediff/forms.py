from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import WhatTheUser

class RegistrationForm(UserCreationForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #password1 = forms.CharField()
    #password2 = forms.CharField()

    class Meta:
        model = WhatTheUser
        fields = ['email', 'first_name', 'last_name', ]
        #fields = [first_name, last_name, email, password1, password2]

    """def clean(self):
        cleaned_data = super(RegistrationtForm, self).clean()

        if cleaned_data.get('password1') is None \
            or cleaned_data.get('password1') == cleaned_data.get('password2'):

            raise forms.ValidationError('Passwords must be provided and they must match.')
    """