from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
# Create your views here.
import requests
import json
def trae(request):
    # r0 = request.get("https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=31731_1450_31325_21125_31254_30823_26350_22159&hisdata=%5B%7B%22time%22%3A1590552543%2C%22kw%22%3A%22%E5%AD%A6%E4%BF%A1%E7%BD%91%E7%99%BB%E5%BD%95%22%7D%2C%7B%22time%22%3A1590552918%2C%22kw%22%3A%22%E5%AD%A6%E4%BD%8D%E7%BD%91%22%2C%22fq%22%3A2%7D%2C%7B%22time%22%3A1590555404%2C%22kw%22%3A%22%E4%B8%AD%E5%85%AC%E6%95%99%E8%82%B2%22%7D%2C%7B%22time%22%3A1590556095%2C%22kw%22%3A%22%E9%A1%BA%E4%B9%89%E7%A9%BA%E6%B8%AF%22%7D%2C%7B%22time%22%3A1590556100%2C%22kw%22%3A%22%E9%A1%BA%E4%B9%89%E7%A9%BA%E6%B8%AF%20%E7%A4%BE%E5%B7%A5%22%7D%2C%7B%22time%22%3A1590556176%2C%22kw%22%3A%22%E9%A1%BA%E4%B9%89%20%E7%A4%BE%E5%B7%A5%22%7D%2C%7B%22time%22%3A1590556200%2C%22kw%22%3A%22%E7%BD%91%E5%8F%8B%E5%81%B6%E9%81%87%E9%83%91%E6%81%BA%E8%8B%97%E8%8B%97%E9%80%9B%E5%85%AC%E5%9B%AD%22%7D%2C%7B%22time%22%3A1591252253%2C%22kw%22%3A%22scf-fi-sme%22%7D%2C%7B%22time%22%3A1591252290%2C%22kw%22%3A%22scf-fi-sme.ft%22%2C%22fq%22%3A3%7D%2C%7B%22time%22%3A1591323852%2C%22kw%22%3A%22scf-gi-sme.ft%22%7D%5D&req=2&csor=0")
    r0 = requests.get("http://192.168.10.18:8580/api/providers")

    data1=r0.json()
    print(data1)

    return JsonResponse({"data":data1})