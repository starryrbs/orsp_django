from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from orsp_django import settings
import uuid
from file.models import *
import json
# Create your views here.
def uploadFile(request):
    # 此处可以接收文件和字符串
    f1 = request.FILES['usericon']
    print(f1)
    # 文件名
    filename=str(uuid.uuid4())+'.'+f1.name.split('.')[1]
    fname = '{0}/pic/{1}'.format(settings.STATICFILES_DIRS[0],filename)
    '''
    fname = '%s/pic/%s' % (settings.STATICFILES_DIRS[0], str(uuid.uuid4())+'.'+f1.name.split('.')[1])
    '''
    print(fname)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return JsonResponse({
        "name":filename
    })

# 设置保存的文件名
def saveFile(request):
    print(json.loads(request.body))
    data=json.loads(request.body)
    print("data",data)
    res=Resource.objects.create(**data)
    return HttpResponse("ok")
# 下载文件
def downloadFile(request):
    return HttpResponse("下载文件")

# 取消上传的文件
def cancelfile(request):
    pass

# 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
def showfile(request):
    pass

# 评论资源功能
def commentFile(request):
   pass

# 添加收藏
def addCollect(request):
    pass

# 取消收藏
def cancelCollect(request):
    pass

# 检测文件重复(根据标题)
def detectionRepetition(request):
    pass