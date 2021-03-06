# Generated by Django 3.0.7 on 2020-08-13 10:01

from django.db import migrations, models
import django.utils.timezone
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('articles', '0004_testimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimage',
            name='myfield',
            field=markdownx.models.MarkdownxField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimage',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='testimage',
            name='img',
            field=models.ImageField(upload_to='img/%Y/%M/%d/'),
        ),
    ]
