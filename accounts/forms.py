from django import forms
from .models import *
from django.forms import ModelForm

class AddDetailsForm(ModelForm):
    class Meta:
        model=Bank
        fields=['name','acno','ifsc','mob','pic']