
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from . import views
app_name="resource"
urlpatterns = [
    # 获取商品类型
    url(r'^getgoodtypetwo/',views.getGoodTypeTwo ,name="getgoodtype"),
    # 获取三级类型
    url(r'^getgoodtypethree/(?P<good_type>.*)',views.getGoodTypeThree ,name="getgoodtype"),
    # 到mongodb拿到商品数据
    url(r'^getgoods', views.getGoods, name="getgoods"),
    # 添加收藏
    url(r'^addcollect/',views.addCollect ,name="addcollect"),
    url(r'^cancelcollect/',views.cancelCollect ,name="cancelcollect"),
    # 上传商品
    url(r'^uploadgoods/',views.uploadGoods ,name="uploadgoods"),
    # 上传商品
    url(r'^searchGoods/', views.searchGoods, name="uploadgoods"),
    # 查看用户上传的商品
    url(r'^seegoodsbyid/', views.seeGoodsById, name="seeGoodsById"),
    # 支付担保金
    url(r'^paymentguaranty/', views.paymentGuaranty, name="paymentGuaranty"),

    url(r'^downloadgoods/',views.downloadGoods ,name="downloadgoods"),
    url(r'^generateorder/',views.generateOrder ,name="generateorder"),
    url(r'^showgoods/',views.showGoods ,name="showgoods"),
    url(r'^commentgoods/',views.commentGoods ,name="commentgoods"),
    url(r'insertdata/', views.insertData, name='insertData'),
]

'''
'''