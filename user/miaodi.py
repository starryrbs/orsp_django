#!/usr/bin/python
# -*-coding:utf-8-*-

# 秒嘀短信API实现
# Refer to: http://www.miaodiyun.com/doc/guide.html
import http.client
import urllib.parse, hashlib, datetime, time, json, ssl
ssl._create_default_https_context = ssl._create_unverified_context


# import httplib,  #加载模块


# 发送行业短信
def sendIndustrySms(tos, smsContent):
    # 定义账号和密码，开户之后可以从用户中心得到这两个值
    accountSid = '1159f044d6c84c88bb21634e80e9b370'
    acctKey = '97cb70436dcc4590917cd22e9d8e9831'

    # 定义地址，端口等
    serverHost = "api.miaodiyun.com"
    serverPort = 443
    industryUrl = "/20150822/industrySMS/sendSMS"

    # 格式化时间戳，并计算签名
    timeStamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    rawsig = accountSid + acctKey + timeStamp
    m = hashlib.md5()
    m.update(str(rawsig).encode('utf-8'))
    sig = m.hexdigest()

    # 定义需要进行发送的数据表单
    params = urllib.parse.urlencode({'accountSid': accountSid,
                                     'smsContent': smsContent,
                                     'to': tos,
                                     'timestamp': timeStamp,
                                     'sig': sig})
    # 定义header
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

    # 与构建https连接
    conn = http.client.HTTPSConnection(serverHost, serverPort)

    # Post数据
    conn.request(method="POST", url=industryUrl, body=params, headers=headers)

    # 返回处理后的数据
    response = conn.getresponse()
    # 读取返回数据
    jsondata = response.read().decode('utf-8')

    # 打印完整的返回数据
    print(jsondata)

    # 解析json，获取特定的几个字段
    jsonObj = json.loads(jsondata)
    respCode = jsonObj['respCode']
    print("错误码:", respCode)
    respDesc = jsonObj['respDesc']
    print("错误描述:", respDesc)

    # 关闭连接
    conn.close()


# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
import http.client

from urllib import parse

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account = "C12610735"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "b81e62919820d133547997be465ede93"

def send_sms(text, mobile):
    params = parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str.decode()