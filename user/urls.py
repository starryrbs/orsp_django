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
from django.conf.urls import url
from django.conf.urls import include
from . import views
app_name="user"
urlpatterns = [
    # 登录
    url(r'login/', views.login, name="login"),
    # 判断用户是否存在
    url(r'isexist/',views.isExist,name='isexist'),
    # 注册
    url(r'regist/',views.register,name='regist'),
    # 修改密码
    url(r'changepsd/',views.changePsd,name='changepsd'),
    # # 上传头像 是一个 url地址+图片名字
    url(r'uploadicon/',views.uploadIcon,name='uploadicon'),
    # 用户上传文件
    url(r'uploadfile/',views.uploadFile,name='uploadfile'),
    # 用户下载文件
    url(r'downloadfile/',views.downloadFile,name='downloadfile'),
    # 用户查看积分,头像,名称,等基本信息
    url(r'showuser/',views.showUser,name='showuser'),
    # 给管理员留言功能
    url(r'leaveword/',views.leaveWord,name='leaveword'),
    # 花钱购买积分
    url(r'buyintegral/',views.buyIntegral,name='buyintegral'),
    url(r'insertdata/',views.insertData,name='insertData'),

]
