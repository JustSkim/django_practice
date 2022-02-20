from django.db import models
# 通常在models.py中定义数据库
# Create your models here.
# 注意，定义完我们自己的应用common的model后，要将其加入settings.py中的INSTALLED_APPS

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

# admin.py是应用（我们这里自己创建的新应用common）的管理员配置文件
# 我们在此注册我们定义的model类，这样Django才会知道
from django.contrib import admin
admin.site.register(Customer)