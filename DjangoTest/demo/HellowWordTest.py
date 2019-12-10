# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


'''
这边直接输出
'''
def hello(request):
    return HttpResponse("Hello world ! ")
    # context = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'hello.html', context)



'''
这边使用模板
'''
def hello1(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def index(request):
    return HttpResponse("主页")