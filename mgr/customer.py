from django.http import JsonResponse
#待会要访问的数据类型是Json类型，所以要引入

# 导入Customer
from common.models import Customer

'''
Django 的 url路由功能 不支持 根据 HTTP 请求的方法 和请求体里面的参数 进行路由。

就是不能像下面这样，来根据请求 是 post 还是 get 来 路由

path('customers/', 'app.views.list_customer', method='get'),
path('customers/', 'app.views.add_customer',  method='post'),
因此编写一个函数， 来 根据 http请求的类型 和请求体里面的参数 分发（或者说路由）给 不同的函数进行处理。
'''


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return listcustomers(request)
    elif action == 'add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


#后端只需要根据接口文档， 返回原始数据就行。
#我们可以使用如下的函数来返回数据库的所有的 客户数据信息
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})


#根据接口文档，添加客户数据接口
'''
前端提供的客户资料为：
{
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}
'''
def addcustomer(request):

    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的 对象  
    record = Customer.objects.create(name=info['name'] ,
                            phonenumber=info['phonenumber'] ,
                            address=info['address'])


    return JsonResponse({'ret': 0, 'id':record.id})

def modifycustomer(request):

    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    
    customerid = request.params['id']
    newdata    = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        #修改失败的情况，要返回失败原因
        return  {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        }


    if 'name' in  newdata:
        customer.name = newdata['name']
    if 'phonenumber' in  newdata:
        customer.phonenumber = newdata['phonenumber']
    if 'address' in  newdata:
        customer.address = newdata['address']

    # 注意，一定要执行save才能将修改信息保存到数据库
    customer.save()

    return JsonResponse({'ret': 0})

def deletecustomer(request):

    customerid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        #删除失败的情况，不存在自然就无法删除
        return  {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    customer.delete()

    return JsonResponse({'ret': 0})