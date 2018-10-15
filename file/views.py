from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def uploadFile(request):
    pass

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