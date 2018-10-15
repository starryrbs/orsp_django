from django.db import models
from datetime import datetime

# Create your models here.
# 基本的用户表,用于登录注册
class User(models.Model):
    telephone=models.CharField(unique=True,max_length=11)
    password=models.CharField(max_length=100)
    regist_time=models.DateTimeField(auto_now_add=True)
    one=models.CharField(max_length=50)
    # u_info = models.OneToOneField(to='Info', on_delete=models.CASCADE, default=1)
#
class Info(models.Model):
    user_name=models.CharField(max_length=40)
    # 默认性别是男0  , 1代表是女
    sex=models.BooleanField(max_length=2,default=0)
    level=models.IntegerField(default=1)
    email=models.CharField(max_length=40,null=True)
    icon=models.CharField(max_length=80,null=True)
    one=models.CharField(max_length=50,null=True)
class Province(models.Model):
    province_name=models.CharField(max_length=10)
#     省市外键依赖
class City(models.Model):
    city_name=models.CharField(max_length=10)
    c_p=models.ForeignKey(to=Province,to_field='id',on_delete=models.CASCADE,default=1)

