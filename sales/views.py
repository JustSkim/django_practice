from re import template
import django
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def listorders(request):
    return HttpResponse("下面是系统中所有订单的信息。。。。")

def listorders_sales(request):
    return HttpResponse("你现在所看到的是sales销售人员模块下的二级路由listorders_sales")

# 引入Customer对象定义
from common.models import Customer

# 先定义好HTML模板，下面的%s或者多个%符号（django的模板引擎）就是要填充的，可以看做C语言打印输出的print语句来理解



html_template ='''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>id</th>
        <th>姓名</th>
        <th>电话号码</th>
        <th>地址</th>
        </tr>
        
        {% for customer in customers %}
            <tr>

            {% for name, value in customer.items %}            
                <td>{{ value }}</td>            
            {% endfor %}
            
            </tr>
        {% endfor %}
        
        
        </table>
    </body>
</html>
'''

#如果使用模板引擎，要引入，并对模板字符串进行处理
'''
很多后端框架都提供了一种 模板技术， 可以在html 中嵌入编程语言代码片段， 
用模板引擎（就是一个专门处理HTML模板的库）来动态的生成HTML代码。
Python 中有很多这样的模板引擎 比如 jinja2 、Mako， Django也内置了一个这样的模板引擎。
'''
from django.template import engines
django_engine = engines['django']
html_template = django_engine.from_string(html_template)

def listcustomers(request):
    #返回一个QuerySet对象，包含所有的表纪录
    #每条表纪录都是是一个dict对象
    #key是字段名，value是字段值
    qs = Customer.objects.values()
    '''
objects表示基类（也就是其父类）。objects是Django帮我们自动生成的管理器对象，
通过这个管理器可以实现对数据的查询， objects是models.Manager类的一个对象，如果我们模型类中添加一个models.Manger类或者其子类变量，那么Django就不再帮我们生成默认的objects管理器。
    '''

    # 可以通过 filter 方法加入过滤条件，修改view里面的代码
    # 检查url中是否有参数phoneNumber
    ph =  request.GET.get('phoneNumber',None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phoneNumber=ph)
    '''
    输入localhost:4000/sales/customers/?phoneNumber=1597，数据库中无符合的phoneNumber字段，不返回
    输入localhost:4000/sales/customers/?phoneNumber=159753，返回数据库中符合的字段
    '''

    '''使用django内置模板后就注释掉下面的语句
    # 生成html模板中要插入的html片段内容
    tableContent = ''
    for customer in  qs:
        tableContent += '<tr>'

        for name,value in customer.items():
            tableContent += f'<td>{value}</td>'

        tableContent += '</tr>'

    return HttpResponse(html_template%tableContent)
    #用我们真正要获取得到的内容来填充表格模板
    #"%"是Python风格的字符串格式化操作符，非常类似C语言里的printf ()函数的字符串格式化（C语言中也是使用%）
    '''
    # 传入渲染模板需要的参数
    rendered = html_template.render({'customers':qs})
    return HttpResponse(rendered)