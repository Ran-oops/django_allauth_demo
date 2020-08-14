# from markdownx import forms
from django import forms
from markdownx.fields import MarkdownxFormField

from articles.models import TestImage


class TestImageForm(forms.ModelForm):
    myfield = MarkdownxFormField()

    class Meta:
        fields = ['name', 'myfield']
        model = TestImage
