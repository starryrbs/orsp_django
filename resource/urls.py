
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
    # 查看我的收藏
    url(r'^seemycollect/', views.seeMyCollect, name="seemycollect"),
    # 上传商品
    url(r'^uploadgoods/',views.uploadGoods ,name="uploadgoods"),
    # 搜索商品
    url(r'^searchGoods/', views.searchGoods, name="uploadgoods"),
    # 查看用户上传的商品
    url(r'^seegoodsbyid/', views.seeGoodsById, name="seeGoodsById"),
    # 支付担保金
    url(r'^paymentguaranty/', views.paymentGuaranty, name="paymentGuaranty"),
    # 查看我的订单
    url(r'^seemyorder/', views.seeMyOrder, name="seemyorder"),
    # 删除订单
    url(r'^deletemyorder/', views.deleteMyOrder, name="deletemyorder"),
    # 查看交换请求
    url(r'^seechange/', views.seeChange, name="seechange"),
    # 卖家同意或者拒绝对方订单
    url(r'^selleragree/', views.sellerAgree, name="selleragree"),
    # 买家查询卖家已经同意的订单
    url(r'^showbuy/', views.showBuy, name="showbuy"),

    url(r'^downloadgoods/',views.downloadGoods ,name="downloadgoods"),
    # 生成订单
    url(r'^generateorder/',views.generateOrder ,name="generateorder"),
    url(r'^showgoods/',views.showGoods ,name="showgoods"),
    url(r'^commentgoods/',views.commentGoods ,name="commentgoods"),
    url(r'insertdata/', views.insertData, name='insertData'),
    # 获取国美数据
    url(r'getguomei/', views.getGuoMei, name='getguomei'),
]

'''
'''