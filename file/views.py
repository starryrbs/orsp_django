from django.shortcuts import render
from django.http import HttpResponse
from orsp_django import settings
import uuid
# Create your views here.
def uploadFile(request):
    # 此处可以接收文件和字符串
    f1 = request.FILES['file']
    print(f1)
    fname = '{0}/pic/{1}'.format(settings.STATICFILES_DIRS[0], f1.name)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("成功")

# 设置保存的文件名

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