#在sales销售人员模块的文件夹下创建二级路由表
from django.contrib import admin
from django.urls import path

from sales.views import listcustomers, listorders_sales

urlpatterns = [
    #二级路由表下的链接不用写主路由表中已经写的sales，只写剩下来的部分就可以
    path('listorders_sales/',listorders_sales),
    path('customers/',listcustomers),
]