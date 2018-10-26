from resource.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import time
from utils.mongodb_connect import *
from utils.mongodb_connect import *
import re
import uuid
from orsp_django import settings
from utils.formatDatatime import formDatatime,timestamp_from_objectid
from utils.objectId_time import general_obj_from_time
from bson.objectid import ObjectId
from django.db.models import Q
# Create your views here.
# 获取商品类型
def getGoodTypeTwo(request):
    data = []
    res_type = list(Product_type_one.objects.all().values())
    for res_one in range(len(res_type)):
        print(res_one)
        data.append(res_type[res_one])
        print("res_type[res_one]", res_type[res_one])
        res_two = list(Product_type_two.objects.filter(one_id_id=res_type[res_one]["id"]).values())
        print(res_two)
        data[res_one]["category"] = []
        for r_t in res_two:
            print("r_t", r_t)
            data[res_one]["category"].append({"id": r_t["id"], "name": r_t["product_type"]})

    return HttpResponse(json.dumps(data, ensure_ascii=False))



# 获取三级商品类型
# 请求中包含一个商品二级类型
def getGoodTypeThree(request, good_type):
    if request.method == "GET" and good_type:
        print(good_type)
        data=[]
        ids=str(good_type).split(',')
        for i in range(len(ids)):
            res_two =list(Product_type_two.objects.filter(id=ids[i]).values())
            print(1,res_two)
            if res_two:
                data.append(res_two[0])
                two_id=res_two[0]["id"]
                res_three=list(Product_type_three.objects.filter(two_id_id=two_id).values())
                print(2,res_three)
                data[i]["category"]=res_three
                print(data)

        return HttpResponse(json.dumps(data))
    else:
        return JsonResponse({"code": "510"})


# 添加收藏
# 传过来一个用户id,和商品id
def addCollect(request):
    if request.method=="POST":
        user_id=json.loads(request.body)["user_id"]
        resource_id=json.loads(request.body)["resource_id"]
        print(user_id,resource_id)
        ins={
            "collect_resource_id":resource_id,
            "user_id":user_id
        }
        try:
            res = User_collect.objects.create(**ins)
            print(dir(res))
            return JsonResponse({"code": "209"})
        except Exception as ex:
            return JsonResponse({"code": "409"})

    else:
        # 请求失败
        return JsonResponse({"code":"510"})


# 取消收藏
def cancelCollect(request):
    pass


# 上传商品
# 上传商品要指定一个三级商品类型,价格,图片的url,描述,用户id,上传时间是当前时间,名字
def uploadGoods(request):
    if request.method=="POST":
        try:
            file = request.FILES["good_icon"]
            print(file)
            name = request.POST.get("name")
            title = request.POST.get("title")
            price = request.POST.get("price")
            pnum = request.POST.get("pnum")
            product_type = request.POST.get("product_type")
            description = request.POST.get("description")
            category = request.POST.get("category")
            user_id = request.POST.get("user_id")

            filename = str(uuid.uuid4()) + '.' + file.name.split('.')[1]
            fname = '{0}/pic/{1}'.format(settings.STATICFILES_DIRS[0], filename)
            '''
            fname = '%s/pic/%s' % (settings.STATICFILES_DIRS[0], str(uuid.uuid4())+'.'+f1.name.split('.')[1])
            '''
            print(fname)
            with open(fname, 'wb') as pic:
                for c in file.chunks():
                    pic.write(c)
            product_type_id = None
            try:
                product_type_id = \
                    list(Product_type_three.objects.filter(product_type__contains=product_type).values("id"))[0]["id"]
            except Exception as ex:
                print(ex)
                product_type_id = 1
            print(1111111111, product_type_id)

            ins = {
                "name": name,
                "title": title,
                "price": price,
                "description": description,
                "category": category,
                "product_type_id": product_type_id,
                "user_id": user_id,
                "imgurl":filename
            }
            print(ins)
            Products.objects.create(**ins)
            return JsonResponse({"code": "299"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "499"})
    else:
        # 请求失败
        return JsonResponse({"code":"510"})

# 根据用户id查看用户上传的商品
def seeGoodsById(request):
    if request.method=="POST":
        id = json.loads(request.body)["id"]
        print(id)
    #     去用户上传商品表查询所有的信息
        res=list(Products.objects.filter(user_id=id).values())
        print(1111111111111,res)
        if res:
            print(res)
            res=formDatatime(res)
            print(res[0]["product_type_id"])
            for i in range(len(res)):
                product_type = list(Product_type_three.objects.filter(id=res[i]["product_type_id"]).values())[0][
                    "product_type"]
                print(product_type)
                res[i]["product_type"] = product_type

            print(res)
            return HttpResponse(json.dumps(res))
        else:
            return JsonResponse({"code":"519"})
    else:
        return JsonResponse({"code":"520"})

# 拿到mongodb里面的商品数据
def getGoods(request):
    data = db.taobao_goods.find().limit(20)
    res_data=[]
    for i in data:
        print(i)
        del i["_id"]
        res_data.append(i)
    print(1,res_data)
    return HttpResponse(json.dumps(res_data))

def searchGoods(request):
    print(request.GET.get('good'))
    good=request.GET.get('good')
    index=int(request.GET.get('index'))
    # db.company.find({\$or: [{catagory: “IT”}, {region: “Beijing”}]});
    # find({"$or":[{"catagory":good},{"belong_name":good}]})
    data = db.taobao_goods.find({"$or":[{"belong_to":good},{"belong_name":good},{"title":{"$regex":good}},{"address":good}]}).limit(500).skip(index)
    # aa = db.taobao_goods.find({"$or":[{"belong_to":good},{"belong_name":good},{"title":good},{"address":good}]})
    # print(aa)
    res=list(Products.objects.filter(Q(name=good) | Q(description=good)| Q(title=good)).values())
    for i in res:
        i["Stock"]=i["category"]
        i["payNum"]=i["pnum"]
        i["img_href"]='http://127.0.0.1:8000/media/pic/'+str(i["imgurl"])
        i["sales_num"]=str(i["pnum"])+'人付款'
        product_type=list(Product_type_three.objects.filter(id=i["product_type_id"]).values())[0]
        i["belong_name"]=product_type["product_type"]
        i["belong_to"]=list(Product_type_two.objects.filter(id=product_type["two_id_id"]).values())[0]["product_type"]
        i["shop"]=list(Info.objects.filter(id=i["user_id"]).values())[0]["user_name"]
        i["address"]="江苏苏州"
        i["change"]="打印机"
        i["user"]=i["user_id"]
    print("----------------")
    print(res)
    '''
    这是查询用户上传的商品信息 [{'id': 16, 'name': '苹果', 'price': 10050.0,
     'category': 10, 'title': 'iphone', 'pnum': 0, 
     'imgurl': 'da369ba8-1858-4d28-b9d9-bac9a96d3194.jpeg',
      'description': '最新版', 'user_id': 14, 
      'upload_time': datetime.datetime(2018, 10, 23, 23, 15, 44, 83074),
       'product_type_id': 271}]
{'_id': ObjectId('5bb596e3923ce03158259063'), 'detail_href': 'https://item.taobao.com/item.htm?id=571762300469&ns=1&abbucket=18#detail', 'belong_to': '明星网红', 'sales_num': '3人付款', 'price': '30.50', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/3877671787/TB20aedqyCYBuNkSnaVXXcMsVXa_!!3877671787.jpg_180x180.jpg_.webp', 'title': '明星网红唐嫣同款iphoneX手机壳7plus全包8plus奢华6s潮牌苹果10', 'shop': '知名度一号店291', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}
[{'id': 16, 'name': '苹果', 'price': 10050.0, 'category': 10, 'title': 'iphone', 
'pnum': 0, 'imgurl': 'da369ba8-1858-4d28-b9d9-bac9a96d3194.jpeg',
 'description': '最新版', 'user_id': 14, 'upload_time': datetime.datetime(2018, 10, 23, 23, 15, 44, 83074), 
 'product_type_id': 271, 'store': 10, 'img': 'http://127.0.0.1:8000/media/pic/da369ba8-1858-4d28-b9d9-bac9a96d3194.jpeg',
  'payNum': 0, 'belong_name': '手机支架'}]

    '''

    print("这是查询用户上传的商品信息",res)

    res_data=[]
    for i in data:
        print(i)
        i["_id"]=timestamp_from_objectid(i["_id"])
        print(i["_id"])
        res_data.append(i)
    print(1,res_data)
    res=formDatatime(res)
    res_data.extend(res)
    print("=============")
    print(res_data)
    '''
    [{'_id': 1538598499.0, 'detail_href': 'https://item.taobao.com/item.htm?id=571762300469&ns=1&abbucket=18#detail', 'belong_to': '明星网红', 'sales_num': '3人付款', 'price': '30.50', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/3877671787/TB20aedqyCYBuNkSnaVXXcMsVXa_!!3877671787.jpg_180x180.jpg_.webp', 'title': '明星网红唐嫣同款iphoneX手机壳7plus全包8plus奢华6s潮牌苹果10', 'shop': '知名度一号店291', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614664.0, 'detail_href': 'https://item.taobao.com/item.htm?id=569461883089&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '462人付款', 'price': '962.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i1/3086143272/O1CN011a2cO48zqnrrc11_!!3086143272.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods国行无线蓝牙耳机全新官方原装正品iphonex8p7', 'shop': '沐沐是只卖良心手机小美女', 'address': '浙江 宁波', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614673.0, 'detail_href': 'https://item.taobao.com/item.htm?id=567117296441&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '2802人付款', 'price': '79.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/2210203366/TB23TU8f5MnBKNjSZFzXXc_qVXa_!!2210203366.jpg_180x180.jpg_.webp', 'title': '无线蓝牙挂脖式运动跑步oppo手机华为防水入耳式iphone8X耳机通用', 'shop': 'yy贸易代购', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614695.0, 'detail_href': 'https://item.taobao.com/item.htm?id=566377969643&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '406人付款', 'price': '169.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i1/3862426536/O1CN011y9X9FETR4J1a5V_!!3862426536.jpg_180x180.jpg_.webp', 'title': 'DTOOM鹿图568运动蓝牙耳机双耳入耳耳塞防水磁吸苹果安卓iphone8x', 'shop': 'dtoom鹿图科技企业店', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614763.0, 'detail_href': 'https://item.taobao.com/item.htm?id=577403327824&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '516人付款', 'price': '29.90', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/4104763090/O1CN011YhGIkVjS5pJwvu_!!4104763090.jpg_180x180.jpg_.webp', 'title': '运动蓝牙耳机 苹果6s华为iphone7p 迷你跑步耳机无线运动型夹耳式', 'shop': '泰戈侃数码科技', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614768.0, 'detail_href': 'https://item.taobao.com/item.htm?id=576016958964&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '1469人付款', 'price': '38.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/3465687900/TB2hlCxhNtnkeRjSZSgXXXAuXXa_!!3465687900.jpg_180x180.jpg_.webp', 'title': '无线蓝牙耳机双耳迷你iphone耳塞式开车男可接听电话苹果安卓通用', 'shop': '刚开团就卖疯了', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614793.0, 'detail_href': 'https://item.taobao.com/item.htm?id=573221402598&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '4766人付款', 'price': '46.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/750714750/TB2EOihCYGYBuNjy0FoXXciBFXa_!!750714750.jpg_180x180.jpg_.webp', 'title': '苹果无线蓝牙耳机iphone7耳塞式8P耳麦X手机6s通用华为oppo小米vivo超小跑步运动双耳入耳式开车可接听电话', 'shop': 'lzg数码', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615731.0, 'detail_href': 'https://detail.tmall.com/item.htm?id=558862700835&ns=1&abbucket=18', 'belong_to': '淘宝速达', 'sales_num': '710人付款', 'price': '5888.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/1776456424/TB1cG82xnCWBKNjSZFtXXaC3FXa_!!0-item_pic.jpg_180x180.jpg_.webp', 'title': '12期分期【现货发送购机礼】iphone8plus苹果8plus中移动Apple/苹果 iPhone 8 Plus全网通手机中国移动官方店', 'shop': '中国移动官方旗舰店', 'address': '浙江 杭州', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615733.0, 'detail_href': 'https://detail.tmall.com/item.htm?id=558701806092&ns=1&abbucket=18', 'belong_to': '淘宝速达', 'sales_num': '524人付款', 'price': '4888.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/268451883/O1CN011PmSFfarbCg0ry5_!!0-item_pic.jpg_180x180.jpg_.webp', 'title': '【送无线充/送延保/送壳膜/送挂绳】 iphone8 国行 Apple/苹果 iPhone 8 全网通4G手机3/6/12期分期国行苹果8', 'shop': '三际数码官方旗舰店', 'address': '山东 济南', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615734.0, 'detail_href': 'https://detail.tmall.com/item.htm?id=558837233162&ns=1&abbucket=18', 'belong_to': '淘宝速达', 'sales_num': '507人付款', 'price': '5828.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/263726286/TB2mGjObVzqK1RjSZFCXXbbxVXa_!!263726286-0-item_pic.jpg_180x180.jpg_.webp', 'title': '送无线充/送延保/送壳膜12期分期Apple/苹果 iPhone 8 Plus 苹果8p 全网通 iphone8p iphone8plus手机', 'shop': '能良数码官方旗舰店', 'address': '上海', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538616710.0, 'detail_href': 'https://detail.tmall.com/item.htm?id=558767486149&ns=1&abbucket=18', 'belong_to': '三星s7', 'sales_num': '1246人付款', 'price': '128.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/896588234/TB2ZL62bzTpK1RjSZKPXXa3UpXa_!!896588234-0-item_pic.jpg_180x180.jpg_.webp', 'title': 'iphoneX无线充电器XS苹果X手机Max新iPhone快充8Plus专用P正品XR官配R无限s三星s7s8s9安卓通用小米紫米note9', 'shop': '菁创数码专营店', 'address': '上海', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538690818.0, 'detail_href': 'https://item.taobao.com/item.htm?id=558183171954&ns=1&abbucket=3#detail', 'belong_to': '电线', 'sales_num': '197人付款', 'price': '11.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/3042658079/TB2GebiaHtlpuFjSspoXXbcDpXa_!!3042658079.jpg_180x180.jpg_.webp', 'title': '苹果数据线修复热缩管 华为Type-c三星iphone7充电线维修理保护套', 'shop': '深圳市大安科技', 'address': '广东 深圳', 'belong_name': '工具', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598504.0, 'detail_href': 'https://item.taobao.com/item.htm?id=577121921879&ns=1&abbucket=18', 'belong_to': '明星网红', 'sales_num': '2人付款', 'price': '30.50', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/3599423170/O1CN011ZHtzBTxryeOOhK_!!3599423170.jpg_180x180.jpg_.webp', 'title': '明星网红奢华苹果8plus全包7plus手机壳iphoneX潮牌6s唐嫣10', 'shop': 't_1514795607436_030', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598512.0, 'detail_href': 'https://item.taobao.com/item.htm?id=577121921879&ns=1&abbucket=18', 'belong_to': '明星网红', 'sales_num': '2人付款', 'price': '30.50', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i4/3599423170/O1CN011ZHtzBTxryeOOhK_!!3599423170.jpg_180x180.jpg_.webp', 'title': '明星网红奢华苹果8plus全包7plus手机壳iphoneX潮牌6s唐嫣10', 'shop': 't_1514795607436_030', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598545.0, 'detail_href': 'https://item.taobao.com/item.htm?id=570483139442&ns=1&abbucket=18#detail', 'belong_to': '明星网红', 'sales_num': '1人付款', 'price': '30.50', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/198818932/TB2qpcCkNuTBuNkHFNRXXc9qpXa_!!198818932.jpg_180x180.jpg_.webp', 'title': '明星网红唐嫣同款iphoneX手机壳7plus全包8plus奢华6s潮牌苹果10', 'shop': 'a407269519', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598553.0, 'detail_href': 'https://item.taobao.com/item.htm?id=570297053754&ns=1&abbucket=18', 'belong_to': '明星网红', 'sales_num': '0人付款', 'price': '30.50', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/198818932/TB2O_pJtXGWBuNjy0FbXXb4sXXa_!!198818932.jpg_180x180.jpg_.webp', 'title': '明星网红奢华苹果8plus全包7plus手机壳iphoneX潮牌6s唐嫣同款10', 'shop': 'a407269519', 'address': '浙江 金华', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598555.0, 'detail_href': 'https://item.taobao.com/item.htm?id=576525276545&ns=1&abbucket=18', 'belong_to': '明星网红', 'sales_num': '0人付款', 'price': '29.40', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/3927458832/O1CN012F76VaL9tShSsLo_!!3927458832.jpg_180x180.jpg_.webp', 'title': '祖母绿网红同款女夏天苹果x手机壳7plus潮牌明星iphone8挂绳6弘祥', 'shop': '美丽人生金金', 'address': '广东 深圳', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538612577.0, 'detail_href': 'https://item.taobao.com/item.htm?id=570412807421&ns=1&abbucket=18#detail', 'belong_to': '淘宝速达', 'sales_num': '2人付款', 'price': '1879.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i2/3025895606/TB2WGeGsVuWBuNjSszbXXcS7FXa_!!3025895606.jpg_180x180.jpg_.webp', 'title': '淘宝速达 同城自提 Apple/苹果 iPhone 6 苹果6s  iphone 6s plus', 'shop': '长沙建资', 'address': '湖南 长沙', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538612633.0, 'detail_href': 'https://item.taobao.com/item.htm?id=551417861850&ns=1&abbucket=18#detail', 'belong_to': '生活电器', 'sales_num': '10人付款', 'price': '6.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i1/475228921/TB2pXErqgJkpuFjSszcXXXfsFXa_!!475228921.jpg_180x180.jpg_.webp', 'title': 'U-PICK原品生活 iphone充电器头贴纸 手机插头背膜 苹果手机饰品', 'shop': '张家卿的店', 'address': '浙江 杭州', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538612634.0, 'detail_href': 'https://item.taobao.com/item.htm?id=551639602185&ns=1&abbucket=18#detail', 'belong_to': '生活电器', 'sales_num': '4人付款', 'price': '5.60', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/398381779/TB2lbX6qHVkpuFjSspcXXbSMVXa_!!398381779.jpg_180x180.jpg_.webp', 'title': 'U-PICK原品生活 iphone充电器头贴纸 手机插头背膜 苹果手机饰品', 'shop': '小树那个临风', 'address': '天津', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614660.0, 'detail_href': 'https://item.taobao.com/item.htm?id=559964862422&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '3069人付款', 'price': '979.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/2586909304/TB2Pyn3opmWBuNjSspdXXbugXXa_!!2586909304.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods无线耳机iphone8x蓝牙7plus原装正品耳机', 'shop': '千冠电子', 'address': '上海', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614661.0, 'detail_href': 'https://item.taobao.com/item.htm?id=564043247193&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '4054人付款', 'price': '978.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/446381428/O1CN011MQ41vzbw2Dp0D1_!!446381428.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods 无线耳机 AirPods iphoneXS蓝牙耳机原装正品', 'shop': '旺隆数码', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614663.0, 'detail_href': 'https://item.taobao.com/item.htm?id=543707000720&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '1379人付款', 'price': '858.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/1642153065/TB2NjIObgxlpuFjy0FoXXa.lXXa_!!1642153065.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果iphone AirPods无线耳麦 iphone8x国行7plus蓝牙耳机XS', 'shop': 'min大少', 'address': '上海', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614663.0, 'detail_href': 'https://item.taobao.com/item.htm?id=546030970242&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '138人付款', 'price': '975.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/345461635/O1CN011Nws1vupG8NYDpb_!!345461635.jpg_180x180.jpg_.webp', 'title': '【国行现货】苹果/apple airpods iphone8X 7plus xs无线蓝牙耳机', 'shop': '宝贝倾临', 'address': '江苏 南京', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614669.0, 'detail_href': 'https://item.taobao.com/item.htm?id=543237040416&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '359人付款', 'price': '968.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i1/14088776/TB2xqw0aRyWBuNkSmFPXXXguVXa_!!14088776.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods潮人无线智能国行iphoneX87p6s苹果蓝牙耳机', 'shop': 'yunlu777', 'address': '四川 成都', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614672.0, 'detail_href': 'https://item.taobao.com/item.htm?id=565662921530&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '165人付款', 'price': '968.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/54748849/O1CN012FEtF8vxLKHF68I_!!54748849.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果AirPods耳机原装正品无线蓝牙iphoneX7/8p音乐游戏耳机', 'shop': '滴水穿石_888', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614696.0, 'detail_href': 'https://item.taobao.com/item.htm?id=568199202743&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '348人付款', 'price': '962.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/3878154483/TB2TR2InkSWBuNjSszdXXbeSpXa_!!3878154483.jpg_180x180.jpg_.webp', 'title': '苹果/apple iphone XS AirPods无线耳机iphone8x蓝牙原装国行', 'shop': '永拓i8体验店', 'address': '山东 青岛', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614698.0, 'detail_href': 'https://item.taobao.com/item.htm?id=576483864428&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '1996人付款', 'price': '17.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i3/4069561625/TB1nOo0vnCWBKNjSZFtXXaC3FXa_!!0-item_pic.jpg_180x180.jpg_.webp', 'title': '适用于苹果7/8plus/X耳机iphone6s/7P耳塞线控扁头入耳式蓝牙耳麦', 'shop': 'tb782863107', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614726.0, 'detail_href': 'https://item.taobao.com/item.htm?id=547497975865&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '48人付款', 'price': '959.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/678621634/TB2k25adN9YBuNjy0FfXXXIsVXa_!!678621634.jpg_180x180.jpg_.webp', 'title': '国行Apple苹果iphone AirPods无线耳机iphone8x蓝牙7plus原装单支', 'shop': '九佳数码', 'address': '山东 济南', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614741.0, 'detail_href': 'https://item.taobao.com/item.htm?id=575113023124&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '415人付款', 'price': '99.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/3583970946/O1CN011IrJ8jftJMT16co_!!3583970946.jpg_180x180.jpg_.webp', 'title': '双耳蓝牙无线运动耳机苹果6跑步iphone7入耳塞8plus颈挂脖式通用x', 'shop': '新音yinre', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614751.0, 'detail_href': 'https://item.taobao.com/item.htm?id=565669352449&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '66人付款', 'price': '1038.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/3379377937/TB2PPIeh8yWBuNkSmFPXXXguVXa_!!3379377937.jpg_180x180.jpg_.webp', 'title': '国行Apple/苹果 AirPods 无线耳机iphone8x蓝牙7plus原装正品', 'shop': '土木良品店铺', 'address': '湖北 武汉', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614762.0, 'detail_href': 'https://item.taobao.com/item.htm?id=563333894365&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '188人付款', 'price': '318.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/10317547/TB2SFNOEr5YBuNjSspoXXbeNFXa_!!10317547.jpg_180x180.jpg_.webp', 'title': '国行Apple苹果iphone AirPods无线耳机iphone8x蓝牙7plus原装正品', 'shop': 'xiaoyin9931', 'address': '浙江 杭州', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614765.0, 'detail_href': 'https://item.taobao.com/item.htm?id=577354542245&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '71人付款', 'price': '138.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/3885269111/O1CN012HAt0p1fyU7OEv3_!!3885269111.jpg_180x180.jpg_.webp', 'title': '无线苹果蓝牙耳机运动跑步iphone7双耳颈挂脖式入耳头戴耳塞8通用', 'shop': '荣创3c', 'address': '广东 深圳', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614791.0, 'detail_href': 'https://item.taobao.com/item.htm?id=547928180110&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '34人付款', 'price': '999.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/55285307/TB2eJMNX7UkyKJjy1zjXXX1wFXa_!!55285307.jpg_180x180.jpg_.webp', 'title': '【新品】Apple/苹果AirPods无线耳机iphone7 8 X蓝牙耳麦国行原封', 'shop': 'zjdtpprint', 'address': '浙江 杭州', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614798.0, 'detail_href': 'https://item.taobao.com/item.htm?id=548966246918&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '54人付款', 'price': '1058.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i4/71946096/TB2iLhFkgLD8KJjSszeXXaGRpXa_!!71946096.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods无线蓝牙耳机耳麦2 iphone7plus6S 8x智能耳机', 'shop': '苦工的店', 'address': '江苏 南京', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615093.0, 'detail_href': 'https://item.taobao.com/item.htm?id=520836660869&ns=1&abbucket=18#detail', 'belong_to': '蓝牙音箱', 'sales_num': '65人付款', 'price': '399.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/83285505/TB2Gj2Cd46I8KJjy0FgXXXXzVXa_!!83285505.jpg_180x180.jpg_.webp', 'title': 'iphoneX\\8\\7手机蓝牙音箱苹果音响专用低音炮无线充电底座播放器', 'shop': 'minluan00', 'address': '福建 福州', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615726.0, 'detail_href': 'https://item.taobao.com/item.htm?id=570412807421&ns=1&abbucket=18#detail', 'belong_to': '淘宝速达', 'sales_num': '2人付款', 'price': '1879.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/3025895606/TB2WGeGsVuWBuNjSszbXXcS7FXa_!!3025895606.jpg_180x180.jpg_.webp', 'title': '淘宝速达 同城自提 Apple/苹果 iPhone 6 苹果6s  iphone 6s plus', 'shop': '长沙建资', 'address': '湖南 长沙', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615731.0, 'detail_href': 'https://item.taobao.com/item.htm?id=558736654894&ns=1&abbucket=18#detail', 'belong_to': '淘宝速达', 'sales_num': '636人付款', 'price': '3358.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/1806965899/O1CN011tRmqg6lw0DztFO_!!1806965899.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 iPhone 8 Plus 苹果8plus手机 iphone8港版国行美版8P', 'shop': '数码科技1628_1628', 'address': '广东 深圳', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615757.0, 'detail_href': 'https://item.taobao.com/item.htm?id=539914761286&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '1人付款', 'price': '10.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/1748989311/TB2bxiIyYBmpuFjSZFAXXaQ0pXa_!!1748989311.jpg_180x180.jpg_.webp', 'title': '北京苹果客服官方换新服务iphone8xsMax/7plus/8plus以旧换新实体', 'shop': '欧阳晓君0259', 'address': '北京', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615789.0, 'detail_href': 'https://item.taobao.com/item.htm?id=563251417893&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '22人付款', 'price': '979.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/134160544/TB2lPOtj46I8KJjSszfXXaZVXXa_!!134160544.jpg_180x180.jpg_.webp', 'title': '【西安实体】国行Apple苹果iphone AirPods无线蓝牙耳机iphone X', 'shop': 'jiangwenming602', 'address': '陕西 西安', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615817.0, 'detail_href': 'https://item.taobao.com/item.htm?id=562295111152&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '9人付款', 'price': '4788.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/1020976468/O1CN011xeODK3zEUKcciG_!!1020976468.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 iPhone Xs Max双卡iphonexs苹果手机 实体店 免费送货', 'shop': '连轩数码', 'address': '河南 郑州', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615827.0, 'detail_href': 'https://item.taobao.com/item.htm?id=563389803778&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '22人付款', 'price': '80.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i2/1998935889/TB2a3QmIHSYBuNjSspiXXXNzpXa_!!1998935889.jpg_180x180.jpg_.webp', 'title': '天津实体店iphone手机 X/8p/8/7p/7/6sp/6s/6p/6/5s屏幕外屏 总成', 'shop': 'ypp19870703', 'address': '天津', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615857.0, 'detail_href': 'https://item.taobao.com/item.htm?id=577499267961&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '15人付款', 'price': '6188.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/14088776/O1CN012EhSKjAJoKB9jWc_!!14088776.png_180x180.jpg_.webp', 'title': '国行实体Apple/苹果 iPhone Xs Max iphonexs 苹果XR新双卡手机xr', 'shop': 'yunlu777', 'address': '四川 成都', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615858.0, 'detail_href': 'https://item.taobao.com/item.htm?id=564668993490&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '10人付款', 'price': '3780.00', 'img_href': 'https://g-search1.alicdn.com/img/bao/uploaded/i4/i1/136357198/TB2crxXeQfb_uJkHFqDXXXVIVXa_!!136357198.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 iPhone 8 Plus iphone 8 美版 韩版 杭州实体店', 'shop': '雅米1019', 'address': '浙江 杭州', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615861.0, 'detail_href': 'https://item.taobao.com/item.htm?id=560821140114&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '2人付款', 'price': '5950.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i3/292779359/TB2Jip9e98YBeNkSnb4XXaevFXa_!!292779359.jpg_180x180.jpg_.webp', 'title': '实体店现货Apple/苹果 iPhone X iphonex原装正品苹果X港版美版', 'shop': '0尹芙蓉0', 'address': '湖南 长沙', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615872.0, 'detail_href': 'https://item.taobao.com/item.htm?id=560984762059&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '8人付款', 'price': '6300.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/28457762/TB21rqNnTnI8KJjy0FfXXcdoVXa_!!28457762.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 iPhone 4S iPhonex观前实体iphone XS MAX 美版国行', 'shop': 'aceplayer', 'address': '江苏 苏州', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538615882.0, 'detail_href': 'https://item.taobao.com/item.htm?id=561601339969&ns=1&abbucket=18#detail', 'belong_to': '实体商场服务', 'sales_num': '15人付款', 'price': '6680.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i4/274432595/TB2MHtQeRLN8KJjSZFpXXbZaVXa_!!274432595.jpg_180x180.jpg_.webp', 'title': '广州实体国行Apple/苹果 iPhone X 港版iphone8咨询iphone xs max', 'shop': '专卖港机', 'address': '广东 广州', 'belong_name': '手机', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538699339.0, 'detail_href': 'https://item.taobao.com/item.htm?id=549409895540&ns=1&abbucket=3#detail', 'belong_to': '测距仪', 'sales_num': '3人付款', 'price': '469.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/135350856/TB1OiJccN9YBuNjy0FfXXXIsVXa_!!2-item_pic.png_180x180.jpg_.webp', 'title': '台湾ipin镭射光尺 激光测距仪 苹果iphone手机激光尺红外线测量尺', 'shop': 'zhonglou9561', 'address': '广东 深圳', 'belong_name': '五金电子', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538598554.0, 'detail_href': 'https://item.taobao.com/item.htm?id=576634249939&ns=1&abbucket=18', 'belong_to': '明星网红', 'sales_num': '0人付款', 'price': '18.60', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/3927458832/O1CN012F76VWfjsOnnUg9_!!3927458832.jpg_180x180.jpg_.webp', 'title': 'nothing苹果x手机壳iphone7/8/6s/5se/plus网红同款明星风弘祥', 'shop': '美丽人生金金', 'address': '广东 深圳', 'belong_name': '男装', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614659.0, 'detail_href': 'https://item.taobao.com/item.htm?id=543665658908&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '5510人付款', 'price': '980.00', 'img_href': 'https://g-search2.alicdn.com/img/bao/uploaded/i4/i4/645544374/O1CN011iBKqluCTQgd3vh_!!645544374.jpg_180x180.jpg_.webp', 'title': '国行Apple/苹果 AirPods 无线耳机iphone8x蓝牙7plus原装正品xs', 'shop': '世博家园00', 'address': '上海', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'_id': 1538614662.0, 'detail_href': 'https://item.taobao.com/item.htm?id=575591307087&ns=1&abbucket=18#detail', 'belong_to': '蓝牙耳机', 'sales_num': '1698人付款', 'price': '963.00', 'img_href': 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/64963165/O1CN011ZFc0XvX9K4XZvS_!!64963165.jpg_180x180.jpg_.webp', 'title': 'Apple/苹果 AirPods入耳式无线蓝牙耳机 iphone8X 7P国行原封正品', 'shop': '淘淘海涛', 'address': '上海', 'belong_name': '家电', 'change': '休闲裤', 'Stock': 25.0}, {'id': 16, 'name': '苹果', 'price': 10050.0, 'category': 10, 'title': 'iphone', 'pnum': 0, 'imgurl': 'da369ba8-1858-4d28-b9d9-bac9a96d3194.jpeg', 'description': '最新版', 'user_id': 14, 'upload_time': '2018-10-23 23:15:44', 'product_type_id': 271, 'store': 10, 'img': 'http://127.0.0.1:8000/media/pic/da369ba8-1858-4d28-b9d9-bac9a96d3194.jpeg', 'payNum': 0, 'belong_name': '手机支架'}]

    '''


    return HttpResponse(json.dumps(res_data))
# 下架商品
def downloadGoods(request):
    pass


# 生成订单
def generateOrder(request):
    if request.method=="POST":
        sellerSelectGood=json.loads(request.body)["sellerSelectGood"]
        buyerSelectGood=json.loads(request.body)["buyerSelectGood"]
        generateTime=datetime.datetime.now().strftime('%Y-%m-%D %H:%M:%S')
        sellerSelectGood=json.loads(sellerSelectGood)
        buyerSelectGood=json.loads(buyerSelectGood)

        # 卖家是否确定订单 已确认1  未确认0
        sellerSelectGood["status"]=0
        # 保障金是否缴纳  0未交 1 已经缴纳
        sellerSelectGood["guarantyStatus"]=0
        print(type(sellerSelectGood["price"]))
        # 保障金金额默认为对方商品价格的一半
        sellerSelectGood["guaranty"]=float(buyerSelectGood["price"])/2
        buyerSelectGood["status"]=1
        buyerSelectGood["guarantyStatus"]=0
        buyerSelectGood["guaranty"]=float(sellerSelectGood["price"])/2

        data={
            "sellerSelectGood":sellerSelectGood,
            "buyerSelectGood":buyerSelectGood,
            "generateTime":generateTime,
            "id":str(uuid.uuid4())
        }
        print(data)
        res=db.order.insert(data)
        return JsonResponse({"insert_id":data["id"]})
    else:
        return JsonResponse({"code":"520"})

# 支付担保金
def paymentGuaranty(request):
    if request.method=="POST":
        id = json.loads(request.body)["id"]
        selectAddressByUser = json.loads(request.body)["selectAddressByUser"]
        selectExpressByUser = json.loads(request.body)["selectExpressByUser"]
        print(id)
        res=db.order.update({"id": id}, {'$set': {"buyerSelectGood.guarantyStatus": 1,"buyerSelectGood.selectAddressByUser":selectAddressByUser,"buyerSelectGood.selectExpressByUser":selectExpressByUser}})
        print(res)
        return JsonResponse({"code":"215"})
    else:
        return JsonResponse({"code":"520"})
    # 查看商品详情

# 查看我的订单
def seeMyOrder(request):
    id=json.loads(request.body)["id"]
    res=list(db.order.find({"buyerSelectGood.user_id": str(id)}))
    print(res)
    for i in res:
        del i["_id"]
    print(res)
    return HttpResponse(json.dumps(res))
def showGoods(request):
    pass


# 评论商品
def commentGoods(request):
    pass


from pymongo import MongoClient


# 这里是用来插入数据的
def insertData(request):
    import json
    with open('test/good.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            # print(i["name"])
            # one_res=Product_type_one.objects.create(**{"product_type":i["name"]})
            # print(one_res)
            for j in i["category"]:
                res_one = Product_type_one.objects.get(product_type=i["name"])
                # print(1,res_one.id)
                # two_res=Product_type_two.objects.create(**{"one_id_id":res_one.id,"product_type":j})
                # print(222222,two_res)
                #             连接数据库
                conn = MongoClient('123.207.11.101', 27017)
                db = conn.orsp  # 连接mydb数据库，没有则自动创建
                # db.authenticate("root", "123456")
                my_set = db.taobao_type.find({"name": j})
                print(1111111, my_set)
                print(dir(my_set))
                for tt in my_set:
                    res_two = Product_type_two.objects.filter(product_type=tt["name"]).first()
                    print("tt", tt["category"])
                    for z in tt["category"]:
                        two_res = Product_type_three.objects.create(**{"two_id_id": res_two.id, "product_type": z})

    return HttpResponse("成功")
