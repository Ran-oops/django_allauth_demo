from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class MyModelQuerySet(models.query.QuerySet):
    def get_one(self):
        return self.filter(id=1)


class MyModel(models.Model):
    myfield = MarkdownxField()
    objects = MyModelQuerySet.as_manager()

    def get_markdown(self):
        return markdownify(self.myfield)
