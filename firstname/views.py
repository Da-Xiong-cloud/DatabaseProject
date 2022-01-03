import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.middleware.csrf import get_token
from django.views import View

from firstname.models import SecondName, Province

"""
    进行CRSF验证值的申请
"""
def getToken(request):
    token = get_token(request)
    response = HttpResponse(content = json.dumps({'token': token }), content_type="application/json,charset=utf-8",status=200)
    return response

"""
    用于处理各个姓氏的分布数据的相应
    GET:返回地图数据
"""
class Map(View):
    def get(self,request):
        print(request.GET)
        surname = request.GET.get('surname')
        if not surname:
            response = HttpResponse(json.dumps({'err': "没有姓氏"}), status=400)
            return response
        data = SecondName.objects.filter(second_name=surname)
        if data.count() == 0:
            response = HttpResponse(json.dumps({'err': "没有姓氏"}), status=400)
            return response
        data = data[0]
        data.count += 1
        data.save()
        ratio = data.D_surname.all()
        province = Province.objects.all()
        data = []
        Min = 10000
        Max = 0
        for j in province:
            tmp = (ratio & j.D_province.all())[0].ratio * 100
            Min = min(tmp , Min)
            Max = max(tmp , Max)
            data.append({'name' : j.name.split('省')[0] , "value" : tmp})
        response = HttpResponse(json.dumps({'data' : data , "min" : Min , "max" : Max}) , status = 200)
        return response

"""
    用于处理各个姓氏的基本数据的响应
    GET:返回姓氏的六大基本数据
"""
class Surname(View):
    def get(self,request):
        surname = request.GET.get('surname')
        if not surname:
            response = HttpResponse(json.dumps({'err': "没有姓氏"}), status=400)
            return response
        data = SecondName.objects.filter(second_name=surname)
        if data.count() == 0:
            response = HttpResponse(json.dumps({'err': "没有姓氏"}), status=400)
            return response
        content = data[0]
        data = {}
        for i in SecondName._meta.fields:
            data[i.verbose_name] = content.serializable_value(str(i).split('.')[-1])
        response = HttpResponse(json.dumps({'data': data}), status=200)
        return response
