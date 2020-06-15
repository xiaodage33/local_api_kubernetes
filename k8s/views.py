from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
# Create your views here.
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from k8s.api import ssh_link   #导入连接方法
def getLog(request):
    data = ssh_link.ssh_linking("kubectl get pods  --all-namespaces  | sed -e 1d | awk '{print $2','$4}'")

    # data = ssh_link.ssh_linking("kubectl get pods | sed -e 1d | awk '{print $1','$3}'") #单个命名空间
    # print("sss",data)  kubectl get pods  --all-namespaces  | sed -e 1d | awk '{print $2','$3}' #所有命名空间
    get_data = data.split()   #需要转一下
    data_list = []
    for  i in range(len(get_data)):
        if i % 2 == 0:
            dic1 = {}
            dic1['pod'] = get_data[i]
        if i % 2 != 0:
            dic2 = {}
            dic2['status'] =get_data[i]
            x_data = dict(list(dic1.items()) + list(dic2.items()))
            data_list.append(x_data)
    # print("niu",data_list)
    return JsonResponse({'data':data_list})
#跟进pod名字进行查询日志
# kubectl logs  -n `kubectl  get pods --all-namespaces | grep etcd-master| awk '{print $1}'`  etcd-master

@method_decorator(csrf_exempt,name='dispatch')
def getLogInfo(request):
    info = request.body
    info = info.decode()
    cmd_1 = "{print $1}"  #不然命令不识别print $1
    cmd = "kubectl logs  -n `kubectl  get pods --all-namespaces | grep {0} | awk '{1}'`  {0}  --tail 20000 ".format(info,cmd_1)
    # print("命令是",cmd)



    data = ssh_link.ssh_linking(cmd)
    # print("hehhe",data)
    return JsonResponse({'data':data})

#查询pod错误实时到集群查询。。慢。。  仅限scf
def getErrorLog(request):
    #抛出有问题数量
    cmd = "for i in `kubectl get pods -n scf |sed -e 1d | awk '{print $1}'`;do kubectl logs $i -n scf  | grep Exception:  >> /dev/null 2>&1 ; if [ `echo $?` -eq 0 ];then echo $i ;fi  done | wc -l"
    data_num = ssh_link.ssh_linking(cmd)
    #抛出所有错误的pod名字
    cmd1 = "for i in `kubectl get pods -n scf |sed -e 1d | awk '{print $1}'`;do kubectl logs $i -n scf  | grep Exception:  >> /dev/null 2>&1 ; if [ `echo $?` -eq 0 ];then echo $i ;fi  done"

    # data_podname = ssh_link.ssh_linking("kubectl get pods -n scf |sed -e 1d | awk '{print $1}'") #暂时测试所有pod名字抛出来
    data_podname = ssh_link.ssh_linking(cmd1)
    # print("====",data_podname)

    get_data = data_podname.split()  #需要转一下
    # print("哈哈",get_data)
    data_podname_list = []

    for key in get_data:
        # print("乐乐",key)
        dic = {}
        dic['data_podname'] = key
        data_podname_list.append((dic))
        # print(data_podname_list)
    # return JsonResponse({"data": data_podname_list})

    return  JsonResponse({'data_num':data_num,'data_podname':data_podname_list})
# 通过日志过来查看错误的pod 快
def log_error_file(request):

    cmd_num = "ls  /var/ftp/pub/log/scf/  | grep Exception | awk -F '.' '{print $1}' | wc -l"
    data_num = ssh_link.ssh_linking(cmd_num)
    print(data_num)
    cmd = "ls  /var/ftp/pub/log/scf/  | grep Exception | awk -F '.' '{print $1}'"
    get_data = ssh_link.ssh_linking(cmd)
    get_data_ok = get_data.split()  #需要转一下
    data_podname_list = []
    for key in get_data_ok:
        # print("乐乐",key)
        dic = {}
        dic['data_podname'] = key
        data_podname_list.append((dic))

    # print("get_data",data_podname_list)
    return JsonResponse({'data_num':data_num,'data_podname':data_podname_list})