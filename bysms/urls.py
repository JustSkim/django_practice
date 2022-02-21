"""bysms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include 
#include关键字是Django中专门用来针对路由的设计

from sales.views import listorders

#启动静态文件服务
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/',include('sales.urls')),
    
    # 凡是 url 以 api/mgr  开头的，
    # 都根据 mgr.urls 里面的 子路由表进行路由
    path('api/mgr/', include('mgr.urls')),

] + static('/',document_root="./z_dist")
'''
这里加这一个static函数，是为了在url 路由中加入前端静态文件的查找路径。
这样如果 http请求的url 不是以上面数组中的 admin/ sales/ api/mgr/ 等等开头， Django 就会认为是要访问 z_dist目录下面的静态文件。
'''