'''
在 mgr 目录下面添加 urls.py 路由文件， 并 加入如下声明
结合bysms中的urls.py的路由路径，就表示凡是API 请求url为 /api/mgr/customers 的，都交由 我们上面定义的dispatch函数进行分派处理
'''
from django.urls import path
from mgr import customer
urlpatterns = [
    path('customers', customer.dispatcher),
]