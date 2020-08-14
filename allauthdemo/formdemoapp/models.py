from django.db import models

# Create your models here.
class EmpForm(models.Model):
    name = models.CharField(max_length=250, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    salary = models.DecimalField(verbose_name="工资", max_digits=10, decimal_places=10)