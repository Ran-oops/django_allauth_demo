from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import TestImage

admin.site.register(TestImage, MarkdownxModelAdmin)

# Register your models here.
