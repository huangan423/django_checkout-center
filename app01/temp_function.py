from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
import urllib.request
import re

def temp_function(lines):
    content_content = dict()
    content_last = []
    for url in lines:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        title = re.findall('<title>欢迎使用云平台(.+)服务</title>', html)
        if title == None:
            print("title  没有找到")
        else:
            service_name_version = " ".join(title)
            a = service_name_version.split(' ')
            content_content['url'] = url
            content_content['service_name'] = a[0]
            content_content['version'] = a[1]
            content_last.append({'url': content_content['url'], 'service_name': content_content['service_name'],'version': content_content['version']})
    return content_last