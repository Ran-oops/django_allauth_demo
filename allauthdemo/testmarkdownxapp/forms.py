from django import forms

from markdownx.fields import MarkdownxFormField
from testmarkdownxapp.models import MyModel


class MyForm(forms.Form):
    myfield = MarkdownxFormField()
