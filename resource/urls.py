
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views
app_name="resource"
urlpatterns = [
    # 获取商品类型
    url(r'^getgoodtypetwo/',views.getGoodTypeTwo ,name="getgoodtype"),
    url(r'^getgoodtypethree/(?P<good_type>.*)',views.getGoodTypeThree ,name="getgoodtype"),
    # 添加收藏
    url(r'^addcollect/',views.addCollect ,name="addcollect"),
    url(r'^cancelcollect/',views.cancelCollect ,name="cancelcollect"),
    # 上传商品
    url(r'^uploadgoods/',views.uploadGoods ,name="uploadgoods"),
    url(r'^downloadgoods/',views.downloadGoods ,name="downloadgoods"),
    url(r'^generateorder/',views.generateOrder ,name="generateorder"),
    url(r'^showgoods/',views.showGoods ,name="showgoods"),
    url(r'^commentgoods/',views.commentGoods ,name="commentgoods"),
    url(r'insertdata/', views.insertData, name='insertData'),
]
'''




'''