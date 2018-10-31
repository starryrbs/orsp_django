from django.db import models
from user.models import *


# Create your models here.
class Product_type_one(models.Model):
    product_type = models.CharField(unique=True, max_length=11)


class Product_type_two(models.Model):
    product_type = models.CharField(max_length=11)
    one_id = models.ForeignKey(to=Product_type_one, to_field='id', on_delete=models.CASCADE, default=1)


class Product_type_three(models.Model):
    product_type = models.CharField(max_length=11)
    two_id = models.ForeignKey(to=Product_type_two, to_field='id', on_delete=models.CASCADE, default=1)


# 资源详情表
class Products(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField(default=0.00)
    category = models.IntegerField(default=0)
    # 标题
    title=models.CharField(max_length=50,null=True)
    # 销量
    pnum = models.IntegerField(default=0)
    imgurl = models.CharField(max_length=256)
    description = models.CharField(max_length=100)
    # 上传者
    user = models.ForeignKey(to=Info, to_field='id', on_delete=models.CASCADE, default=1)
    upload_time = models.DateTimeField(null=True, auto_now_add=True)
    product_type = models.ForeignKey(to_field='id', to=Product_type_three, on_delete=models.CASCADE, default=1)
    status=models.CharField(max_length=2,default=0)
    # 用户收藏
    # collects=models.ManyToManyField(Info)


class User_collect(models.Model):
    user = models.ForeignKey(to=Info, to_field='id', on_delete=models.CASCADE, default=1)
    collect_resource = models.ForeignKey(to_field='id', to=Products, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = ("user", "collect_resource")


# 订单表

'''
province = models.ForeignKey(Region, related_name='province_houses')  
    city = models.ForeignKey(Region, related_name='city_houses')  
    district = models.ForeignKey(Region, related_name='district_houses')  
'''


# 发送订单叫buyer,接受订单请求的叫seller
class Order(models.Model):
    #     单价
    unitPrice = models.DecimalField(max_digits=11, decimal_places=2)
    seller = models.ForeignKey(Info, related_name='seller_good', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Info, related_name='buyer_good', on_delete=models.CASCADE)
    ordertime = models.DateTimeField(auto_now_add=True)
    sellerAddress = models.ForeignKey(Address, related_name='seller_address', on_delete=models.CASCADE)
    buyerAddress = models.ForeignKey(Address, related_name='buyer_address', on_delete=models.CASCADE)
    sellernum = models.IntegerField(default=1)
    buyernum = models.IntegerField(default=1)
    status=models.CharField(max_length=10,null=True)
#     商品
    good=models.ForeignKey(to=Products,to_field='id',on_delete=models.CASCADE, default=1)

# 订单状态表
class Status(models.Model):
    # 保障金  0 表示买家保障金未交 1表示买家保障金已交 2 表示卖家保障金未交 3表示卖家保障金已交
    guaranty=models.IntegerField(default=0)
    # 状态的名字
    # 交易成功,没有交易,正在交易中
    statusName=models.CharField(max_length=20)


'''
    
'''
