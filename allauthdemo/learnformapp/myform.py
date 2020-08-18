from django import forms
from django.forms import fields

class UserForm(forms.Form):
    username = fields.CharField()
    email = fields.EmailField()