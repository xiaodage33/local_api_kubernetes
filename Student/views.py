from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
# Create your views here.
from .models import  *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import QueryDict
import json

from django.views.decorators.http import require_http_methods


def index(request):

    stu = Student.objects.all().values()
    print(type(list(stu)))
    sms1=sms(request)
    ac = list(stu)
    # print(ac)
    # return render(request,'get.html',{'stu':ac})
    print("====",ac)
    return JsonResponse({'data': ac})

#对vue添加add接口
@method_decorator(csrf_exempt,name='dispatch')
def add(request):

    data=request.body
    print(json.loads(data))

    stu_name = json.loads(data).get('stu_name')
    stu_sex = json.loads(data).get('stu_sex')
    stu_cls_id = json.loads(data).get('stu_cls_id')
    print(stu_name,"==",stu_sex,"==",stu_cls_id)
    stu_add =Student(stu_name= stu_name, stu_sex=stu_sex,stu_cls_id=stu_cls_id)
    stu_add.save()
    return JsonResponse({"message_data":"001"})

# @method_decorator(csrf_exempt,name='dispatch')
# def add(request):
#     stu_name = request.POST.get('stu_name','')
#     stu_sex = request.POST.get('stu_sex','')
#     stu_cls_id = request.POST.get('stu_cls_id','')
#     stu_add =Student(stu_name= stu_name, stu_sex=stu_sex,stu_cls_id=stu_cls_id)
#     stu_add.save()
#     return HttpResponse("ok")

@method_decorator(csrf_exempt,name='dispatch')
def select(request):

    data = request.body #b'{"username":"haha"}' 无法提取
    data = json.loads(data) #
    print("转化为json",data) #{'username': 'haha'}
    if data.get('id'):
        get_stu_id=data.get('id')
        print("===",get_stu_id)
        info = Student.objects.values().filter(id=get_stu_id)[0]
        print("查询all:",info)
        return JsonResponse(info)

    if data.get('username'):
        get_stu_name = data.get('username')
        info = Student.objects.values().filter(stu_name=get_stu_name)[0]
        print("info",info)

        return JsonResponse(info)

    # if get_stu_name == 'haha':
        # return HttpResponse(sms(request))

import random
def sms(request):
    alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890'
    sum_data = "".join(random.sample(alphabet, 8))
    return JsonResponse({"stu_name":sum_data})

@method_decorator(csrf_exempt,name='dispatch')
def del_info(request):
    print("===",request.body)
    del_data = request.body
    print("11",del_data)
    del_da = json.loads(del_data)
    print("22",del_da)
    del_o = del_da.get('id')
    print('33',del_o)

    del_stu = Student.objects.get(id=del_o)
    print(del_stu)
    if del_stu:
        if request.method == 'POST':
            del_stu.delete()
            return JsonResponse({'data':"删除ok"})
    return JsonResponse({'data':'del_error'})


from .form import StudentForm
@method_decorator(csrf_exempt,name='dispatch')

def edit_info(request):
    # 查询到指定的数据
    edit_data = request.body
    data_up = json.loads(edit_data)
    print("修改：",data_up)
    stu_id = data_up.get('id')
    stu_name = data_up.get('stu_name')
    stu_cls_id = data_up.get('stu_cls_id')
    stu_sex = data_up.get('stu_sex')
    update_edit = Student.objects.filter(id=stu_id).update(stu_name=stu_name, stu_sex=stu_sex, stu_cls_id=stu_cls_id)
    if update_edit:
        return JsonResponse({'data':'update ok'})
    else:
        return JsonResponse({'data':'update error'})
    # #表单形式
    # print("===",request.body)
    # edit_stu = Student.objects.get(id=article_id)
    # if request.method != 'POST':
    #     # 如果不是post,创建一个表单，并用instance=article当前数据填充表单
    #     form = StudentForm(instance=edit_stu)
    # else:
    #     # 如果是post,instance=article当前数据填充表单，并用data=request.POST获取到表单里的内容
    #     form = StudentForm(instance=edit_stu, data=request.POST)
    #     form.save()  # 保存
    #     if form.is_valid():  # 验证
    #         return JsonResponse({'data':"修改ok"})  # 成功跳转
    # return JsonResponse({'data':'error'})