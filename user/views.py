from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from user.models import *
import json
import re
from werkzeug.security import generate_password_hash, check_password_hash
from utils.token_get import *
from orsp_django import settings
import random, time, pymysql
from .miaodi import *
connection = pymysql.Connect(
            host='cdb-4hg425ql.gz.tencentcdb.com',
            port=10034,
            user='root',
            passwd='13866015127rbs',
            db='dj_orsp',
            charset='utf8'
        )
from django.db.models import Q
from utils.mongodb_connect import *


# Create your views here.
def login(request):
    print(request.body)
    if request.method == "POST":
        print(json.loads(request.body))
        telephone = json.loads(request.body)["telephone"]
        res_user = list(User.objects.filter(telephone=telephone).values())
        if len(res_user) == 1:
            print(1111, res_user)
            password = json.loads(request.body)["password"]
            print(password)
            print(res_user[0]["password"])
            # 校验密码
            res_psd = check_password_hash(res_user[0]["password"], password)
            print(res_psd)
            if res_psd:
                res_token = jwtEncoding({"telephone": telephone, "password": password})
                print("token", res_token)
                # 生成token
                response = JsonResponse({"code": "206"})
                response["token"] = res_token
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
        return JsonResponse({"code": "510"})


# 验证用户是否已存在
def isExist(request):
    if request.method == "POST":
        telephone = json.loads(request.body)["telephone"]
        res = User.objects.filter(telephone=telephone)
        print(res)
        if len(res) == 1:
            # 用户已存在
            return JsonResponse({"code": "208"})
        else:
            # 用户不存在
            return JsonResponse({"code": "408"})
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 判断token是否正确
def judgeToken(request):
    if request.method == "POST":
        # try:
        token = request.META.get("HTTP_TOKEN")
        print("进入judgeToken方法，token", token)
        # 拿token中的数据
        SECRECT_KEY = "orsp"
        data = jwt.decode(str(token).encode(), SECRECT_KEY, audience='webkit', algorithms=['HS256'])
        print(data['some']["telephone"])
        telephone = data['some']["telephone"]
        res = list(User.objects.filter(telephone=telephone).values())
        print(res[0]["id"])
        res_data = list(Info.objects.filter(id=res[0]["id"]).values())
        print(res_data)
        print("end judgeToken")
        if res_data:
            return JsonResponse({"id": res_data[0]["id"], "user_name": res_data[0]["user_name"]})
        else:
            return JsonResponse({"code": "517"})
    # except Exception as ex:
    #     print(ex)
    #     return JsonResponse({"code": "517"})
    else:
        return JsonResponse({"code": "517"})


# 用户注册
def register(request):
    # 账号注册,需要用户名,密码,手机号
    if request.method == "POST":
        # 验证手机号
        reg = r'^1[34578]\d{9}$'
        print(json.loads(request.body))
        telephone = json.loads(request.body)["telephone"]
        if re.match(reg, telephone):
            password = json.loads(request.body)["password"]
            try:
                if len(password) >= 6:
                    password = generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)

                    user_name = json.loads(request.body)["user_name"]
                    ins_info = {
                        "user_name": user_name
                    }
                    res_in_info = Info.objects.create(**ins_info)
                    ins_user = {
                        "telephone": telephone,
                        "password": password,
                    }

                    res_in_user = User.objects.create(**ins_user)

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
                print("错误是", ex)
                return JsonResponse({"code": "405"})
        else:
            # 手机号不合法
            return JsonResponse({"code": "512"})
    else:
        # 请求失败
        return JsonResponse({"code": "请求失败"})


# 修改密码
def changePsd(request):
    if request.method == "POST":
        req = json.loads(request.body)
        password = User.objects.filter(telephone=req['telephone']).values("password")[0]["password"]
        res_psd = check_password_hash(password, req['current_password'])
        if res_psd:
            if req['new_password'] == req['new_password_verify']:
                a = User.objects.get(telephone=req['telephone'])

                a.password = generate_password_hash(req['new_password'], method='pbkdf2:sha1:2000', salt_length=8)
                a.save()
                # 修改成功

                return JsonResponse({"code": "211"})
            else:

                # 两次密码不一致
                return JsonResponse({"code": "516"})
        else:

            # 用户密码错误
            return JsonResponse({"code": "514"})
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 渲染头像 是一个 图片名字
def getUsericon(request):
    if request.method == 'POST':
        try:
            getlist = json.loads(request.body)

            # print(job)
            # res就是正在插入的对象
            # res = models.job.objects.create(**job)
            # print(res.id)
            qid = User.objects.filter(telephone=getlist['telephone']).values('id')
            qid = qid[0]['id']
            a = Info.objects.get(id=qid)
            a.icon = getlist['icon']
            a.save()
            return JsonResponse({"code": "218"})
        except Exception as ex:
            return JsonResponse({"code": "515"})
    else:
        return JsonResponse({"code": "510"})


def changeaddress(request):
    if request.method == 'POST':
        getdata = json.loads(request.body)
        index = getdata['index']
        # Address.objects.filter(user_id=getdata['id']).update(default='0')
        Address.objects.filter(user_id=getdata['userid']).update(default='0')
        Address.objects.filter(id=getdata['id']).update(default='1')
    else:
        return JsonResponse({"code": "510"})


def deladdress(request):
    if request.method == 'POST':
        getdata = json.loads(request.body)
        print(getdata)
        print('sssssssssssssssss',getdata['userid'], getdata['id'])
        Address.objects.filter(id=getdata['id']).delete()
    else:
        return JsonResponse({"code": "510"})


# 根据用户id查询用户地址
def getAddresById(request):
    if request.method == "POST":
        id = json.loads(request.body)
        id = id['id']
        # 去查询手机号
        res = list(Address.objects.filter(user_id=id).values())
        for r in res:
            r["provice_id"] = list(Province.objects.filter(id=r["provice_id"]).values('province_name'))[0][
                "province_name"]
            r["city_id"] = list(City.objects.filter(id=r["city_id"]).values('city_name'))[0]["city_name"]

        return HttpResponse(json.dumps(res))
    else:
        return JsonResponse({"code": "510"})


# 确认支付担保金
def generateGuaranty(request, money):
    context = {}
    context["money"] = money
    return render(request, 'index.html', context=context)


def acquireGuaranty(request):
    if request.method == "POST":
        money = json.loads(request.body)["money"]
        return HttpResponse('<a>ok</a>')
    else:
        return JsonResponse({"code": "510"})


# 用户上传文件
def uploadFile(request):
    pass


# 用户下载文件
def downloadFile(request):
    pass


# 用户查看积分,头像,名称,等基本信息
def showUser(request):
    try:
        if request.method == 'GET':

            token = request.META.get("HTTP_TOKEN")
            SECRECT_KEY = "orsp"
            data = jwt.decode(str(token).encode(), SECRECT_KEY, audience='webkit', algorithms=['HS256'])
            telephone = data["some"]["telephone"]
            qid = User.objects.filter(telephone=telephone).values('id')
            qid = qid[0]['id']
            data = Info.objects.filter(id=qid).values('user_name', 'level', 'email', 'icon', 'sex', 'integral', 'one')[0]
            data1 = data  # 这里必须声明一个新数组，不然是无法改变sex里面的值
            data1["telephone"] = telephone
            if not data["sex"]:
                data1["sex"] = "男"
            else:
                data1["sex"] = "女"
            if not data["email"]:
                data1["email"] = "尚未绑定邮箱"

            if qid:
                return JsonResponse(data1)
            else:
                return JsonResponse({"code": "515"})
    except Exception as ex:
        return JsonResponse({"code": "510"})


# 给管理员留言功能
def leaveWord(request):
    pass


# 花钱购买积分
def buyIntegral(request):
    pass


# 修改个人信息

def changeMsg(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)

            user_name = data["name"]
            telephone = data["telephone"]

            user_id = User.objects.filter(telephone=telephone).values("id")[0]['id']

            email = data["email"]
            if email == "尚未绑定邮箱":
                email = None
            level = data["level"]
            icon = data["icon"]
            sex = data["sex"]
            QQ = data["QQ"]
            integral = data["integral"]
            if sex == "男":
                sex = 0
            else:
                sex = 1
            res = Info.objects.filter(id=user_id).update(user_name=user_name, email=email, level=level, icon=icon,
                                                         sex=sex, integral=integral, one=QQ)
            print(res)  # 如果修改成功
            return JsonResponse({"code": "修改成功"})
        else:
            return JsonResponse({"code": "修改失败"})
    except Exception as e:
        print(2222, e)


# 验证密码
def verifyPassword(request):
    try:
        if request.method == "POST":
            req = json.loads(request.body)
            tel = req["telephone"]
            current_password = req["current_password"]
            print(current_password)
            password = User.objects.filter(telephone=tel).values("password")[0]["password"]
            res = check_password_hash(password, current_password)
            if res:
                return JsonResponse({"code": "255"})  # 255代表验证密码成功
            else:
                return JsonResponse({"code": "455"})  # 455代表验证密码失败
        else:
            return JsonResponse({"code": "404"})
    except Exception as e:
        print("verifyPassword>>>>" + e)


# 上传头像
def uploadUsericon(request):
    import uuid

    if request.method == "POST":
        try:
            # 此处可以接收文件和字符串
            f1 = request.FILES["usericon"]
            token = request.META.get("HTTP_TOKEN")
            SECRECT_KEY = "orsp"
            data = jwt.decode(str(token).encode(), SECRECT_KEY, audience='webkit', algorithms=['HS256'])
            telephone = data["some"]["telephone"]
            userid = User.objects.filter(telephone=telephone).values("id")[0]["id"]
            # 文件名
            filename = str(uuid.uuid4()) + '.' + f1.name.split('.')[1]
            # 设置保存的文件名
            fname = "{0}/pic/{1}".format(settings.STATICFILES_DIRS[0], filename)

            with open(fname, 'wb')as pic:
                for c in f1.chunks():
                    pic.write(c)
            res = Info.objects.filter(id=userid).update(icon=filename)
            if res:
                return JsonResponse({"filename": filename, "code": "218"})
                # return JsonResponse({"filename": fname, "code":"218"}) # 图片在后台服务器里放着
        except Exception as e:

            return JsonResponse({"code": "418"})
    else:
        return JsonResponse({"code:": "418"})


# 获得省市二级联动
def getCityProvince(request):
    data = []
    province = Province.objects.all().values()
    for i in range(len(province)):
        data.append(province[i])
        city = list(City.objects.filter(c_p_id=province[i]["id"]).values())
        data[i]["city"] = city

    return HttpResponse(json.dumps(data))


# 添加用户收货地址
def addAddress(request):
    if request.method == "POST":
        user_id = json.loads(request.body)["user_id"]
        connect_name = json.loads(request.body)["concact_name"]
        concact_telephone = json.loads(request.body)["concact_telephone"]
        city_id = json.loads(request.body)["city_id"]
        provice_id = json.loads(request.body)["provice_id"],
        default = json.loads(request.body)["default"],
        ins_data = {
            "user_id": user_id,
            "concact_name": connect_name,
            "concact_telephone": concact_telephone,
            "city_id": city_id,
            "provice_id": provice_id[0],
        }
        if default[0]:
            Address.objects.filter(user_id=user_id).update(default=0)
            ins_data["default"] = 1
        else:
            ins_data["default"] = 0
        res = Address.objects.create(**ins_data)

        return JsonResponse({"code": "287"})
    else:
        # 请求失败
        return JsonResponse({"code": "510"})


# 这里是用来插入数据的

# 短信验证码
def sendcode(request):
    '''
    :param          mobile
    :return:        (1): code:412       手机号码输入不正确，或者已被注册
                    (2): code:200       发送短信成功
    '''


    # print(now_date + 60)
    #
    # timeArray = time.localtime(now_date)
    #
    # otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    #
    # print(otherStyleTime)

    if request.method == "POST":
        mobile = json.loads(request.body)["phone"]


        # if form.validate():
        #

        code=random.randrange(1000,9999)
        code=str(code)
        print(code)
        smsContent='【ORSP】您的验证码为{0}，请于{1}分钟内正确输入，如非本人操作，请忽略此短信。'.format(code,5)
        text = "您的验证码是：{}。请不要把验证码泄露给其他人。".format(code)
        # print(11111111111)
        print(111111111111111,text,mobile)
        print(send_sms(text, mobile))
        # sendIndustrySms(mobile,smsContent)
        print(2222222222222)

        # #将获取到的验证码存储到数据库中
        now_date = time.time() + 120

        cursor = connection.cursor()

        sql = "DELETE from securty WHERE telephone = {0}".format(mobile)

        n = cursor.execute(sql)

        sql = "insert into securty() VALUE({0},{1},{2},{3})".format(mobile,code,now_date,1)

        bb = cursor.execute(sql)

        print(1111111)
        return JsonResponse({'code': 200, 'message': '发送成功'})
        # else:
        #     message = form.errors.popitem()[1][0]                 #弹出第一条验证失败错误信息
        #     print(type(jsonify({'code':406})))
        #     return JsonResponse({'code':412,'message':message})
        # response=JsonResponse({'code':200,'message':'发送成功'})
        # response['Access-Control-Allow-Origin']='*'


def yezheng(request):

    now_dates = time.time()

    mobble = json.loads(request.body)

    mobbl = int(mobble['phone'])
    yecode = int(mobble["yecode"])

    print(yecode)
    try:
        cursor = connection.cursor()

        sql = "select * from securty WHERE telephone = {0}".format(mobbl)

        bb = cursor.execute(sql)

        res = cursor.fetchone()


        if (res[1] == yecode) and (float(res[2]) >= now_dates):

            sql = "UPDATE securty set state = 2 WHERE telephone = {0}".format(mobbl)
            bb = cursor.execute(sql)
            r = {"code":200}
        else:
            r = {"code":403}

        return JsonResponse(r)

    except Exception as ex:
        print(ex)

def insertData(request):
    import json
    with open('test/p_c.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            # print(i["city"])
            for j in i["city"]:
                p_id = Province.objects.get(province_name=i["name"])
                t = {
                    "city_name": j["name"],
                    "c_p_id": p_id.id
                }

                c = City.objects.create(**t)

    return HttpResponse("成功")


'''
token {'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID_SDK_HOME': 'D:\\android-sdk-windows', 'APPDATA': 'C:\\Users\\raobaoshi\\AppData\\Roaming', 'ASL.LOG': 'Destination=file', 'AWE_DIR': 'C:\\Program Files (x86)\\Khrona LLC\\Awesomium SDK\\1.6.6\\', 'CLASSPATH': '.;C:\\Program Files\\Java\\jdk1.8.0_111\\lib\\dt\\.jar;C:\\Program Files\\Java\\jdk1.8.0_111\\lib\\tools.jar;;C:\\Program Files\\Java\\jdk1.8.0_111\\lib', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ASUS', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FP_NO_HOST_CHECK': 'NO', 'GTK_BASEPATH': 'C:\\Program Files (x86)\\GtkSharp\\2.12\\', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\raobaoshi', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_111', 'LOCALAPPDATA': 'C:\\Users\\raobaoshi\\AppData\\Local', 'LOGONSERVER': '\\\\ASUS', 'M2_HOME': 'D:\\apache-maven-3.3.9', 'MAVEN_HOME': 'D:\\apache-maven-3.3.9', 'MOZ_PLUGIN_PATH': 'D:\\soft\\Foxit Reader\\plugins\\', 'NUMBER_OF_PROCESSORS': '4', 'ONEDRIVE': 'C:\\Users\\raobaoshi\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'D:\\oracle\\app\\oracle\\product\\10.2.0\\server\\bin;C:\\Program Files\\Java\\jdk1.8.0_111\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\system32\\wbem;C:\\Program Files (x86)\\GtkSharp\\2.12\\bin;D:\\android-sdk-windows\\platform-tools;D:\\android-sdk-windows\\tools;C:\\Program Files\\MySQL\\MySQL Server 5.7\\bin;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;";D:\\AutoTestPlatform\\php";C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\dotnet\\;D:\\AutoTestPlatform\\mysql\\bin;D:\\oracle\\app\\oracle\\product\\10.2.0\\server\\BIN;D:\\apache-maven-3.3.9\\bin;C:\\Users\\raobaoshi\\AppData\\Local\\Programs\\Python\\Python36\\Scripts;C:\\Users\\raobaoshi\\PycharmProjects\\learn\\venv\\Scripts\\scrapy.exe;D:\\MongoDB\\bin;D:\\Django project\\venv\\Scripts;C:\\Windows\\System32\\OpenSSH\\;D:\\xampp\\mysql\\bin;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\soft\\Git\\cmd;C:\\Users\\raobaoshi\\AppData\\Local\\Programs\\Python\\Python36\\;D:\\soft\\nodejs\\;C:\\Program Files (x86)\\Microsoft VS Code\\bin;C:\\Users\\raobaoshi\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\raobaoshi\\AppData\\Local\\Programs\\Fiddler;C:\\Users\\raobaoshi\\AppData\\Local\\Programs\\Python\\Python36\\Scripts;D:\\Django project\\venv\\Scripts;;C:\\Users\\raobaoshi\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\raobaoshi\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC.PY;.PYM;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '3c03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PT5HOME': 'D:\\soft\\Cisco Packet Tracer 6.0', 'PT6HOME': 'D:\\soft\\Cisco Packet Tracer 6.0', 'PTYHONPATH': 'D:\\machine learning\\machine learning\\k-近邻算法', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_PORT': '54989', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\soft\\PyCharm 2018.1.4\\helpers\\pycharm_matplotlib_backend;D:\\orsp\\orsp_django', 'PYTHONUNBUFFERED': '1', 'QT_QPA_PLATFORM_PLUGIN_PATH': 'C:\\Users\\raobaoshi\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\plugins', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\RAOBAO~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\RAOBAO~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'asus', 'USERDOMAIN_ROAMINGPROFILE': 'asus', 'USERNAME': 'raobaoshi', 'USERPROFILE': 'C:\\Users\\raobaoshi', 'WINDIR': 'C:\\Windows', 'DJANGO_SETTINGS_MODULE': 'orsp_django.settings', 'RUN_MAIN': 'true', 'SERVER_NAME': 'asus', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '249', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/user/judgetoken/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'application/json;charset=UTF-8', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_ACCEPT': 'application/json, text/plain, */*', 'HTTP_ORIGIN': 'http://localhost:8080', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 'HTTP_REFERER': 'http://localhost:8080/', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'wsgi.input': <_io.BufferedReader name=1064>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
'''
