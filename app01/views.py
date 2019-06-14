from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from app01 import temp_function
import urllib.request
import re

# Create your views here.
def test_148(request):
    lines = ['http://192.168.5.148:60001', 'http://192.168.5.148:60002', 'http://192.168.5.148:60003','http://192.168.5.148:60004', 'http://192.168.5.148:60005', 'http://192.168.5.148:60006','http://192.168.5.148:60008', 'http://192.168.5.148:60011', 'http://192.168.5.148:60014','http://192.168.5.148:60016', 'http://192.168.5.148:60019', 'http://192.168.5.148:60021','http://192.168.5.148:60023', 'http://192.168.5.148:60025', 'http://192.168.5.148:60026','http://192.168.5.148:60032']
    content_last = temp_function.temp_function(lines)
    return render(request, "test.html", {"list": content_last})

def test__148(request):
    lines = ['http://192.168.1.148:60001','http://192.168.1.148:60002','http://192.168.1.148:60003','http://192.168.1.148:60004','http://192.168.1.148:60005','http://192.168.1.148:60006','http://192.168.1.148:60008','http://192.168.1.148:60011','http://192.168.1.148:60014','http://192.168.1.148:60016','http://192.168.1.148:60019','http://192.168.1.148:60021','http://192.168.1.148:60023','http://192.168.1.148:60025','http://192.168.1.148:60026']
    content_last = temp_function.temp_function(lines)
    return render(request,"test.html",{"list":content_last})

def sumer(request):
    return render(request,"base.html")