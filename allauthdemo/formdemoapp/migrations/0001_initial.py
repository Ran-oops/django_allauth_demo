# Generated by Django 3.0.7 on 2020-08-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('salary', models.DecimalField(decimal_places=10, max_digits=10, verbose_name='工资')),
            ],
        ),
    ]
