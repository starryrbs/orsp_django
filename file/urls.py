"""orsp_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views
app_name="file"
urlpatterns = [
    # 这里是上传文件已经成功,存储文件信息与用户信息
    url(r'^uploadfile/',views.uploadFile,name="uploadfile"),
    # 保存文件的信息
    url(r'^savefile/',views.saveFile,name="uploadfile"),
    # # 下载文件
    url(r'^downloadfile',views.downloadFile,name="downloadfile"),
    # # 取消上传的文件
    url(r'^cancelfile',views.cancelfile,name="cancelfile"),
    # # 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
    url(r'^showfile',views.showfile,name="showfile"),
    # 评论资源功能
    url(r'^commentfile',views.commentFile,name="commentfile"),
    # 添加收藏
    url(r'^addcollect',views.addCollect,name="addcollect"),
    # 取消收藏
    url(r'^cancelcollect',views.cancelCollect,name="cancelcollect"),
    # 检测文件重复(根据标题)
    url(r'^detectionrepetition',views.detectionRepetition,name="detectionrepetition"),
]
'''


'''