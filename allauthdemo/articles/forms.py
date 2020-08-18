# from markdownx import forms
from django import forms as dform
from markdownx.fields import MarkdownxFormField

from articles.models import TestImage


class TestImageForm(dform.ModelForm):
    myfield = MarkdownxFormField()

    class Meta:
        fields = ['name', 'myfield']
        model = TestImage
