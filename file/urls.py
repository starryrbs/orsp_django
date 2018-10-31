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
    # 这里是上传文件已经成功,存储文件信息与用户信息 我的上传
    url(r'^uploadfile/',views.uploadFile,name="uploadfile"),
    # 保存文件的信息
    url(r'^savefile/',views.saveFile,name="uploadfile"),
    # # 下载文件
    url(r'^downloadfile/',views.downloadfile,name="downloadfile"),
    # 判断是否允许下载文件
    url(r'^checkdownloadfile/',views.checkdownloadfile,name="checkdownloadfile"),
    # 取消上传的文件
    url(r'^cancelfile/',views.cancelfile,name="cancelfile"),
    # 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
    url(r'^showfile/',views.showfile,name="showfile"),
    # 查看已下载文件
    url(r'^showdownloadfile/', views.showDownloadFile, name="showdownloadfile"),
    # 判断是否已下载
    url(r'^whetherdownload/', views.whetherdownload, name="whetherdownload"),
    # 查看上传文件
    url(r'^showmyupfile',views.showmyupfile,name="showmyupfile"),
    # 评论资源功能
    url(r'^commentfile/',views.commentFile,name="commentfile"),
    # 添加收藏
    url(r'^addcollect/',views.addCollect,name="addcollect"),
    # 取消收藏
    url(r'^cancelcollect/',views.cancelCollect,name="cancelcollect"),
    # 收藏人数
    url(r'^collectnumber/',views.collectnumber,name="collectnumber"),
    # 已收藏文件
    url(r'^showcollectfile/(?P<id>\d*)/',views.showCollectFile,name="showcollectfile"),
    # 我发布的文件
    url(r'^getmyuploadfile/',views.getMyUploadFile,name="getMyUploadFile"),
    # 检测文件重复(根据标题)
    url(r'^detectionrepetition/',views.detectionRepetition,name="detectionrepetition"),
    # 删除上传文件
    url(r'^delmyupfile/',views.delmyupfile,name="delmyupfile"),
    # 查看所有用户上传的文件
    url(r'^showallfile/', views.showAllFile, name="showallfile"),
    # 查看所有用户上传的文件bytwoField
    url(r'^showfilebycondition/', views.showFileByCondition, name="showfilebycondition"),
    # 拿到技术领域一级类型
    url(r'^gettechnicalfield/', views.getTechnicalField, name="gettechnicalfield"),
    # 拿到技术领域一级类型
    url(r'^gettwotechnicalfield/', views.getTwoTechnicalField, name="gettwotechnicalfield"),
    # 拿到资源类型
    url(r'^getresourcetype/', views.getResourceType, name="getresourcetype"),
    # 技术领域二级联动
    url(r'^getalltechnicalfield/', views.getAllTechnicalField, name="getalltechnicalfield"),
]
'''


'''