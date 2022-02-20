from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def listorders(request):
    return HttpResponse("下面是系统中所有订单的信息。。。。")

def listorders_sales(request):
    return HttpResponse("你现在所看到的是sales销售人员模块下的二级路由listorders_sales")

# 引入Customer对象定义
from common.models import Customer
def listcustomers(request):
    #返回一个QuerySet对象，包含所有的表纪录
    #每条表纪录都是是一个dict对象
    #key是字段名，value是字段值
    qs = Customer.objects.values()
    '''
objects表示基类（也就是其父类）。objects是Django帮我们自动生成的管理器对象，
通过这个管理器可以实现对数据的查询， objects是models.Manager类的一个对象，如果我们模型类中添加一个models.Manger类或者其子类变量，那么Django就不再帮我们生成默认的objects管理器。
    '''

    #定义返回字符串
    retStr = ''
    for customer in qs:
        for name,value in customer.items():
            retStr += f'{name}:{value}|'

        #<br>表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
