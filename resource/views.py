from resource.models import *
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from utils.mongodb_connect import *
from utils.mongodb_connect import db
import re
from utils.formatDatatime import formDatatime

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
        user_id=json.loads(request.body)["user_id"]
        product_type_id=json.loads(request.body)["product_type_id"]
        price=json.loads(request.body)["price"]
        description=json.loads(request.body)["description"]
        name=json.loads(request.body)["name"]
        img_url=json.loads(request.body)["img_url"]
        ins={
            "name":name,
            "user_id":user_id,
            "description":description,
            "price":price,
            "product_type_id":product_type_id,
            "imgurl":img_url
        }
        res=Products.objects.create(**ins)
        print(res)
        return JsonResponse({"code":"test"})
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
            return HttpResponse(json.dumps(res))
        else:
            return JsonResponse({"code":"519"})
    else:
        return JsonResponse({"code":"518"})

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
    res_data=[]
    for i in data:
        print(i)
        del i["_id"]
        res_data.append(i)
    print(1,res_data)
    return HttpResponse(json.dumps(res_data))
# 下架商品
def downloadGoods(request):
    pass


# 生成订单
def generateOrder(request):
    pass


# 查看商品详情
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
