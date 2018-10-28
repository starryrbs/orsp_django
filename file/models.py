from django.db import models
from user.models import User
# Create your models here.
# 资源类型表
class ResourceType(models.Model):
    name=models.CharField(max_length=20)

# 技术领域表
class TechnicalField(models.Model):
    name=models.CharField(max_length=20)

# 二级技术领域表
class TwoTechnicalField(models.Model):
    name=models.CharField(max_length=20)
    technicalFieldId=models.ForeignKey(to=TechnicalField,to_field='id',on_delete=models.CASCADE,default=1)


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
    describe=models.CharField(null=True,max_length=80)
    resourceTypeId=models.ForeignKey(to=ResourceType,to_field='id',on_delete=models.CASCADE,default=1)
    twoTechnicalFieldId=models.ForeignKey(to=TwoTechnicalField,to_field='id',on_delete=models.CASCADE,default=1)
    # 用户收藏表
class Collect(models.Model):
    user=models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,default=1)
    resource=models.ForeignKey(to=Resource,to_field='id',on_delete=models.CASCADE,default=1)
    
# 用户下载文件资源表
class Download(models.Model):
    user=models.ForeignKey(to=User,to_field='id',on_delete=models.CASCADE,default=1)
    file=models.ForeignKey(to=Resource,to_field='id',on_delete=models.CASCADE,default=1)

