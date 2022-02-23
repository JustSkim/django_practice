from django.db import models
# 通常在models.py中定义数据库
# Create your models here.
# 注意，定义完我们自己的应用common的model后，要将其加入settings.py中的INSTALLED_APPS
import datetime
class Customer(models.Model):
    #第一个字段是integer类型的varchar，我们这里不指定也会棒我们生成

    #客户名称，数据类型是django中的charfield
    name = models.CharField(max_length=200)

    #联系电话
    phoneNumber = models.CharField(max_length=200)

    #地址
    address = models.CharField(max_length=300)

    #qq
    qq = models.CharField(max_length=20,null=True,blank=True)
    #null=True允许为空，blank=True允许为空白字符串！


#定义 药品（Medicine） 这张表，包括药品名称、编号和描述 这些信息
class Medicine(models.Model):
    # 药品名
    name = models.CharField(max_length=200)
    # 药品编号
    sn = models.CharField(max_length=200)
    # 描述
    desc = models.CharField(max_length=200)

'''
定义 订单 表 Order，
其中客户字段就应该是一个外键，对应Customer表的主键，也就是id字段
Django中定义外键 的方法就是 Model类的该属性字段 值为 ForeignKey 对象，如下所示
'''
class Order(models.Model):
    # 订单名
    name = models.CharField(max_length=200,null=True,blank=True)

    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)

    # 客户
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    # 订单购买的药品，和Medicine表是多对多 的关系
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')



class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # 订单中药品的数量
    amount = models.PositiveIntegerField()


# admin.py是应用（我们这里自己创建的新应用common）的管理员配置文件
# 我们在此注册我们定义的model类，这样Django才会知道
from django.contrib import admin
admin.site.register(Customer)