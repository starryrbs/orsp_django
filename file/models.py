from django.db import models
from user.models import User
# Create your models here.

# 这是文件资源的信息表
class Resource(models.Model):
    # 后面要加上评论id
    # content=models.CharField(max_length=256,null=True)
    name=models.CharField(max_length=40,null=True)
    download_count=models.IntegerField(default=0)
    need_integral=models.IntegerField(default=0)
    upload_user=models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,default=1)
    upload_time=models.DateTimeField(auto_now_add=True)
    # introduce=models.CharField(null=True,max_length=80)
    like_num=models.IntegerField(default=0)
    share_num=models.IntegerField(default=0)
    title=models.CharField(null=True,max_length=80)
#     用户收藏表
class Collect(models.Model):
    user=models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,default=1)
    resource=models.ForeignKey(to=Resource,to_field='id',on_delete=models.CASCADE,default=1)
