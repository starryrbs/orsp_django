from django.db import models
from user.models import *
# Create your models here.
class Product_type_one(models.Model):
    product_type=models.CharField(unique=True,max_length=11)
class Product_type_two(models.Model):
    product_type=models.CharField(max_length=11)
    one_id=models.ForeignKey(to=Product_type_one,to_field='id',on_delete=models.CASCADE,default=1)
class Product_type_three(models.Model):
    product_type=models.CharField(max_length=11)
    two_id=models.ForeignKey(to=Product_type_two,to_field='id',on_delete=models.CASCADE,default=1)
#资源详情表
class Products(models.Model):
    name=models.CharField(max_length=15)
    price=models.FloatField(default=0.00)
    category=models.IntegerField(default=0)
    # 销量
    pnum=models.IntegerField(default=0)
    imgurl=models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    # 上传者
    user=models.ForeignKey(to=Info,to_field='id',on_delete=models.CASCADE,default=1)
    upload_time=models.DateTimeField(null=True,auto_now_add=True)
    product_type=models.ForeignKey(to_field='id',to=Product_type_three,on_delete=models.CASCADE,default=1)
    # 用户收藏
    # collects=models.ManyToManyField(Info)
class User_collect(models.Model):
    user=models.ForeignKey(to=Info,to_field='id',on_delete=models.CASCADE,default=1)
    collect_resource=models.ForeignKey(to_field='id',to=Products,on_delete=models.CASCADE,default=1)
    class Meta:
        unique_together = ("user", "collect_resource")

'''
    
'''