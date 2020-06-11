from django.forms import ModelForm
from .models import Student,Class

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['id','stu_name','stu_sex','stu_cls']