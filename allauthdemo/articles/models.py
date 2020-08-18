from django.db import models
from django.conf import settings
import django.utils.timezone as timezone
# from django.utils.timezone.now()
from markdownx.utils import markdownify
from taggit.managers import TaggableManager
from markdownx.models import MarkdownxField
# from markdown.util import markdownify
# Create your models here.
class NewArticle(models.Model):
    STATUS = (
        ("D","Draft"),
        ("P","Published")
    )
    title = models.CharField(max_length=255, null=False, unique=True, verbose_name='文章标题')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="author", on_delete=models.SET_NULL, verbose_name='作者')
    image = models.ImageField(upload_to='articles/%Y/%M/%d/', verbose_name='文章图片')
    status = models.CharField(max_length=1, choices=STATUS, default='D', verbose_name='状态')
    edited = models.BooleanField(default=False, verbose_name='是否可编辑')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '文章'
        db_table='new_article'
        verbose_name_plural=verbose_name
        ordering = ("created_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return self.title


class TestImage(models.Model):
    name = models.CharField(max_length=150, null=True)
    img = models.ImageField(upload_to='img/%Y/%M/%d/')
    tags = TaggableManager()
    myfield = MarkdownxField()

    class Meta:
        db_table='ImageStore'

    # def __str__(self):
    #     return self.myfield

    def get_markdown(self):
        '''markdown->html'''
        return markdownify(self.myfield)