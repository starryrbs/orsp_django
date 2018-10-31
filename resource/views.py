from resource.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import time
from utils.mongodb_connect import *
import re
import uuid
from orsp_django import settings
from utils.formatDatatime import formDatatime, timestamp_from_objectid
from utils.objectId_time import general_obj_from_time
from bson.objectid import ObjectId
from django.db.models import Q
import bson


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
        data = []
        ids = str(good_type).split(',')
        for i in range(len(ids)):
            res_two = list(Product_type_two.objects.filter(id=ids[i]).values())
            print(1, res_two)
            if res_two:
                data.append(res_two[0])
                two_id = res_two[0]["id"]
                res_three = list(Product_type_three.objects.filter(two_id_id=two_id).values())[0:20]
                print(2, res_three)
                data[i]["category"] = res_three
                print(data)

        return HttpResponse(json.dumps(data))
    else:
        return JsonResponse({"code": "510"})


# 添加收藏
# 传过来一个用户id,和商品id
def addCollect(request):
    if request.method == "POST":
        user_id = json.loads(request.body)["user_id"]
        resource_id = json.loads(request.body)["resource_id"]
        operation = json.loads(request.body)["operation"]
        ins = {
            "collect_resource_id": resource_id,
            "user_id": user_id,
        }
        # operation为1代表收藏
        # try:
        if str(ins["collect_resource_id"]).__len__() < 10:
            print("----------10----------------")
            if operation == 1:
                res = User_collect.objects.create(**ins)
                print(res)
            else:
                res = User_collect.objects.filter(user_id=ins["user_id"],
                                                  collect_resource_id=ins["collect_resource_id"]).delete()
                print(res)
        else:
            if operation == 1:
                res = db.collect.insert(ins)
            else:
                db.collect.remove({"user_id": ins["user_id"], "collect_resource_id": ins["collect_resource_id"]}, True)
        return JsonResponse({"code": "209"})
        # except Exception as ex:
        #     return JsonResponse({"code": "409"})

    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 取消收藏
def cancelCollect(request):
    pass


# 查看我的收藏
def seeMyCollect(request):
    if request.method == "POST":
        user_id = json.loads(request.body)["user_id"]
        res = list(User_collect.objects.filter(user_id=user_id).values())
        print(res)
        res_mon = list(db.collect.find({"user_id": user_id}))
        print(res_mon)
        # # 返回的数据
        data = []
        for i in res:
            print()
            res_id = i["collect_resource_id"]
            good = list(Products.objects.filter(id=res_id).values())[0]
            data.append(good)
        print(data)
        data = formDatatime(data)
        for i in res_mon:
            del i["_id"]
        if "show" in json.loads(request.body):
            print("--------------在这里面----------")
            for i in range(len(res)):
                collect_good = list(Products.objects.filter(id=res[i]["collect_resource_id"]).values())[0]
                res[i]["name"] = collect_good["name"]
                print("collect_good", collect_good)
                res[i]["img_src"] = '/media/pic/' + collect_good["imgurl"]

            for i in range(len(res_mon)):
                collect_good = list(db.taobao_goods.find({"_id": ObjectId(str(res_mon[i]["collect_resource_id"]))}))[0]
                res_mon[i]["name"] = collect_good["title"]
                res_mon[i]["img_src"] = collect_good["img_href"]
        res.extend(res_mon)
        print(res)
        print(json.loads(request.body))

        return HttpResponse(json.dumps(res))
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 上传商品
# 上传商品要指定一个三级商品类型,价格,图片的url,描述,用户id,上传时间是当前时间,名字
def uploadGoods(request):
    if request.method == "POST":
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
                product_type_id = list(Product_type_three.objects.filter(product_type__contains=product_type).values("id"))[0]["id"]
            except Exception as ex:
                print(ex)
                product_type_id = 312
            print(1111111111, product_type_id)

            ins = {
                "name": name,
                "title": title,
                "price": price,
                "description": description,
                "category": category,
                "product_type_id": product_type_id,
                "user_id": user_id,
                "imgurl": filename
            }
            print(ins)
            Products.objects.create(**ins)
            return JsonResponse({"code": "299"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "499"})
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 根据用户id查看用户上传的商品
def seeGoodsById(request):
    if request.method == "POST":
        id = json.loads(request.body)["id"]
        print(id)
        #     去用户上传商品表查询所有的信息
        res = list(Products.objects.filter(user_id=id).values())
        print(1111111111111, res)
        if res:
            print(res)
            res = formDatatime(res)
            print(res[0]["product_type_id"])
            for i in range(len(res)):
                product_type = list(Product_type_three.objects.filter(id=res[i]["product_type_id"]).values())[0][
                    "product_type"]
                print(product_type)
                res[i]["product_type"] = product_type

            print(res)
            return HttpResponse(json.dumps(res))
        else:
            return JsonResponse({"code": "519"})
    else:
        return JsonResponse({"code": "520"})


# 拿到mongodb里面的商品数据
def getGoods(request):
    data = db.taobao_goods.find().limit(20)
    res_data = []
    for i in data:
        print(i)
        del i["_id"]
        res_data.append(i)
    print(1, res_data)
    return HttpResponse(json.dumps(res_data))


def searchGoods(request):
    print(1111111,request.GET.get('good'))
    good = request.GET.get('good')
    index = int(request.GET.get('index'))
    try:
        max_price = request.GET.get('max_price')
        min_price = request.GET.get('min_price')
        print(max_price,min_price)
        data = db.taobao_goods.find(
            {"$or": [{"belong_to": good}, {"belong_name": good}, {"title": {"$regex": good}}, {"address": good}],"price":{"$gt":float(min_price),"$lt":float(max_price)}}).limit(500).skip(index)

    except Exception as ex:
        print("出现错误",ex)
        data = db.taobao_goods.find(
            {"$or": [{"belong_to": good}, {"belong_name": good}, {"title": {"$regex": good}}, {"address": good}]}).sort(
            [("title", 1)]).limit(500).skip(index)
    # db.company.find({\$or: [{catagory: “IT”}, {region: “Beijing”}]});
    # find({"$or":[{"catagory":good},{"belong_name":good}]})
    # data = db.taobao_goods.find(
    #     {"$or": [{"belong_to": good}, {"belong_name": good}, {"title": {"$regex": good}}, {"address": good}]}).sort(
    #     [("title", 1)]).limit(500).skip(index)
    # aa = db.taobao_goods.find({"$or":[{"belong_to":good},{"belong_name":good},{"title":good},{"address":good}]})
    # print(aa)
    res = list(Products.objects.filter(
        Q(name__icontains=good) | Q(description__icontains=good) | Q(title__icontains=good)).values())
    for i in res:
        i["Stock"] = i["category"]
        i["payNum"] = i["pnum"]
        i["img_href"] = '/media/pic/' + str(i["imgurl"])
        i["sales_num"] = str(i["pnum"]) + '人付款'
        product_type = list(Product_type_three.objects.filter(id=i["product_type_id"]).values())[0]
        i["belong_name"] = product_type["product_type"]
        i["belong_to"] = list(Product_type_two.objects.filter(id=product_type["two_id_id"]).values())[0]["product_type"]
        i["shop"] = list(Info.objects.filter(id=i["user_id"]).values())[0]["user_name"]
        i["address"] = "江苏苏州"
        i["change"] = "打印机"
        i["user"] = i["user_id"]
        i["_id"] = i["id"]
    print("----------------")
    print(res)

    print("这是查询用户上传的商品信息", res)

    res_data = []
    for i in data:
        print(i)
        i["_id"] = bson.objectid.ObjectId(i["_id"]).__str__()
        print(i["_id"])
        res_data.append(i)
    print(1, res_data)
    res = formDatatime(res)
    res_data.extend(res)
    print("=============")
    print(res_data)

    return HttpResponse(json.dumps(res_data))


# 下架商品
def downloadGoods(request):
    pass


# 生成订单
def generateOrder(request):
    if request.method == "POST":
        sellerSelectGood = json.loads(request.body)["sellerSelectGood"]
        buyerSelectGood = json.loads(request.body)["buyerSelectGood"]
        generateTime = datetime.datetime.now().strftime('%Y-%m-%D %H:%M:%S')
        sellerSelectGood = json.loads(sellerSelectGood)
        buyerSelectGood = json.loads(buyerSelectGood)

        # 卖家是否确定订单 已确认1  未确认0
        sellerSelectGood["status"] = 0
        # 保障金是否缴纳  0未交 1 已经缴纳
        sellerSelectGood["guarantyStatus"] = 0
        print(type(sellerSelectGood["price"]))
        # 保障金金额默认为对方商品价格的一半
        sellerSelectGood["guaranty"] = float(buyerSelectGood["price"]) / 2
        buyerSelectGood["status"] = 1
        buyerSelectGood["guarantyStatus"] = 0
        buyerSelectGood["guaranty"] = float(sellerSelectGood["price"]) / 2

        data = {
            "sellerSelectGood": sellerSelectGood,
            "buyerSelectGood": buyerSelectGood,
            "generateTime": generateTime,
            "id": str(uuid.uuid4())
        }
        print(data)
        res = db.order.insert(data)
        return JsonResponse({"insert_id": data["id"]})
    else:
        return JsonResponse({"code": "520"})


# 支付担保金
def paymentGuaranty(request):
    if request.method == "POST":
        id = json.loads(request.body)["id"]
        selectAddressByUser = json.loads(request.body)["selectAddressByUser"]
        selectExpressByUser = json.loads(request.body)["selectExpressByUser"]
        print("id是",id)
        res = db.order.update({"id": id}, {
            '$set': {"buyerSelectGood.guarantyStatus": 1, "buyerSelectGood.selectAddressByUser": selectAddressByUser,
                     "buyerSelectGood.selectExpressByUser": selectExpressByUser}})
        print(res)
        return JsonResponse({"code": "215"})
    else:
        return JsonResponse({"code": "520"})
    # 查看商品详情


# 查看我的订单
def seeMyOrder(request):
    id = json.loads(request.body)["id"]
    res = list(db.order.find({"buyerSelectGood.user_id": str(id)}))
    print(res)
    for i in res:
        del i["_id"]
    print(res)
    return HttpResponse(json.dumps(res))
def deleteMyOrder(request):
    if request.method == "POST":
        id = json.loads(request.body)["id"]
        user_id = json.loads(request.body)["user_id"]
        res = db.order.remove({"id": str(id),"buyerSelectGood.user_id":user_id})
        return HttpResponse("ok")
    else:
        # 请求失败
        return JsonResponse({"code": "510"})

def showGoods(request):
    pass


# 评论商品
def commentGoods(request):
    pass


#
def seeChange(request):
    user_id = json.loads(request.body)["user_id"]
    res = list(db.order.find({"sellerSelectGood.user": str(user_id)}))
    print(res)
    for i in res:
        i["_id"] = timestamp_from_objectid(i["_id"])
    print(1111111111, res)
    return HttpResponse(json.dumps(res))



# 卖家同意交换请求
def sellerAgree(request):
    if request.method == "POST":
        user_id = json.loads(request.body)["user_id"]
        operation = json.loads(request.body)["operation"]
        _id = json.loads(request.body)["_id"]
        print(_id)
        #     operation为1代表同意请求，操作码为-1代表拒绝
        res = db.order.update({"sellerSelectGood.user": str(user_id), "sellerSelectGood._id": _id},
                              {'$set': {"sellerSelectGood.status": int(operation)}})
        print(res)
        return JsonResponse({"code": "298"})
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


from pymongo import MongoClient


# 查询买家已经买到的订单，就是卖家已经同意
def showBuy(request):
    if request.method == "POST":
        user_id = json.loads(request.body)["user_id"]
        print(user_id)
        #     operation为1代表同意请求，操作码为-1代表拒绝
        res = list(db.order.find({"buyerSelectGood.user_id": user_id, "sellerSelectGood.status": 1}))
        print(res)
        for i in res:
            del i["_id"]

        return HttpResponse(json.dumps(res))
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


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


# 获取国美数据
def getGuoMei(request):
    # res=db.guomei.find()
    # print(res)
    # res_data=[]
    # for i in res:
    #     print(i)
    #     i["_id"]=timestamp_from_objectid(i["_id"])
    #     print(i["_id"])
    #     res_data.append(i)
    with open('resource/data/data.json', 'r', encoding='utf-8') as f:
        res_data = f.read()
    return HttpResponse(res_data)
