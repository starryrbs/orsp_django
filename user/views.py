from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from user.models import *
import json
import re
from werkzeug.security import generate_password_hash,check_password_hash
from utils.token_get import *
# Create your views here.
def login(request):
    print(request.body)
    if request.method=="POST":
            print(json.loads(request.body))
            telephone=json.loads(request.body)["telephone"]
            res_user = list(User.objects.filter(telephone=telephone).values())
            if len(res_user)==1:
                print(1111,res_user)
                password = json.loads(request.body)["password"]
                print(password)
                print(res_user[0]["password"])
                # 校验密码
                res_psd=check_password_hash(res_user[0]["password"],password)
                if res_psd:
                    res_token = jwtEncoding({"telephone":telephone,"password":password})
                    # 生成token
                    response=JsonResponse({"code":"206"})
                    response["token"]=res_token
                    response["Access-Control-Allow-Headers"] = "Token"
                    response["Access-Control-Expose-Headers"] = "Token"
                    return response
                else:
                    return JsonResponse({"code": "514"})
            else:
                return JsonResponse({"code": "408"})
            # 去数据库查询用户名密码匹配
    else:
        # 请求失败
        return JsonResponse({"code":"510"})

# 验证用户是否已存在
def isExist(request):
    if request.method=="POST":
        telephone=json.loads(request.body)["telephone"]
        res=User.objects.filter(telephone=telephone)
        print(res)
        if len(res)==1:
            # 用户已存在
            return JsonResponse({"code":"208"})
        else:
            # 用户不存在
            return JsonResponse({"code":"408"})
    else:
        # 请求失败
        return JsonResponse({"code":"510"})
# 用户注册
def register(request):
    print(111111111111111111)
    # 账号注册,需要用户名,密码,手机号
    if request.method=="POST":
        # 验证手机号
        reg = r'^1[34578]\d{9}$'
        print(json.loads(request.body))
        telephone=json.loads(request.body)["telephone"]
        if re.match(reg,telephone):
            password=json.loads(request.body)["password"]
            try:
                if len(password) >= 6:
                    password = generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
                    print(password)
                    user_name = json.loads(request.body)["user_name"]
                    ins_info = {
                        "user_name": user_name
                    }
                    res_in_info = Info.objects.create(**ins_info)
                    ins_user = {
                        "telephone": telephone,
                        "password": password,
                    }
                    print("要插入用户表的数据", ins_user)
                    res_in_user = User.objects.create(**ins_user)
                    print(res_in_user)
                    print("ins_info", ins_info, "ins_user", ins_user)
                    res_token = jwtEncoding(ins_user)
                    # 生成token
                    response = JsonResponse({"code": "205"})
                    response["token"] = res_token
                    response["Access-Control-Allow-Headers"] = "Token"
                    response["Access-Control-Expose-Headers"] = "Token"
                    return response
                else:
                    # 密码不合法
                    return JsonResponse({"code": "511"})
            except Exception as ex:
                print("错误是",ex)
                return JsonResponse({"code": "405"})
        else:
            # 手机号不合法
            return JsonResponse({"code": "512"})
    else:
        # 请求失败
        return JsonResponse({"code": "请求失败"})

#修改密码
def changePsd(request):
    pass

# 上传头像 是一个 url地址+图片名字
def uploadIcon(request):
    pass

# 用户上传文件
def uploadFile(request):
    pass

# 用户下载文件
def downloadFile(request):
    pass

# 用户查看积分,头像,名称,等基本信息
def showUser(request):
    pass

# 给管理员留言功能
def leaveWord(request):
    pass

# 花钱购买积分
def buyIntegral(request):
    pass



# 这里是用来插入数据的


def insertData(request):
    import json
    with open('test/p_c.json','r',encoding='utf-8') as f:
        data=json.load(f)
        for i in data:
            # print(i["city"])
            for j in i["city"]:
                print(i)
                print(i["name"],j["name"])
                p_id=Province.objects.get(province_name=i["name"])
                t={
                    "city_name":j["name"],
                    "c_p_id":p_id.id
                }
                print(1,t)
                c=City.objects.create(**t)
                print(2,c)
    return HttpResponse("成功")
