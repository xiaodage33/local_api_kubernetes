from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Class(models.Model):
    cls_name = models.CharField(max_length=10,verbose_name="班级")


class Student(models.Model):
    stu_name = models.CharField(max_length=30,verbose_name="名字")
    stu_sex = models.IntegerField(default=0,verbose_name="性别0是女")
    stu_cls = models.ForeignKey(Class,on_delete=models.CASCADE)
