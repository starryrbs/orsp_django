from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from orsp_django import settings
import uuid
from file.models import *
from user.models import *
import json
from django.http import FileResponse
from utils.formatDatatime import *

# Create your views here.
def uploadFile(request):
    # 此处可以接收文件和字符串
    f1 = request.FILES['usericon']
    print(f1)
    # 文件名
    filename = str(uuid.uuid4()) + '.' + f1.name.split('.')[1]
    fname = '{0}/pic/{1}'.format(settings.STATICFILES_DIRS[0], filename)
    '''
    fname = '%s/pic/%s' % (settings.STATICFILES_DIRS[0], str(uuid.uuid4())+'.'+f1.name.split('.')[1])
    '''
    print(fname)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return JsonResponse({
        "name": filename
    })


# 设置保存的文件名
def saveFile(request):
    print(json.loads(request.body))
    data = json.loads(request.body)
    print("data", data)
    resourceTypeId_id=list(ResourceType.objects.filter(name=data["resourceType"]).values())[0]["id"]
    data["resourceTypeId_id"]=resourceTypeId_id
    del data["resourceType"]
    data["share_num"]=0
    data["like_num"]=0
    print(data)
    res = Resource.objects.create(**data)
    return HttpResponse("ok")


# 判断是否允许下载文件
def checkdownloadfile(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        need = Resource.objects.filter(upload_user_id=request_data['upuserid']).values('need_integral')[0][
            'need_integral']
        if int(request_data['myid']) - need:
            return JsonResponse({"code": 214})
        else:
            return JsonResponse({"code": 410})
    else:
        return JsonResponse({"code": "510"})

# 下载文件
def downloadfile(request):
    if request.method == "POST":
        filename = json.loads(request.body)
        if filename['fname']:
            # media / pic
            filepath = ('media/pic/{0}'.format(filename['fname']))
            response = FileResponse(readFile(filepath))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename['fname'])
            return response
    else:
        return JsonResponse({"code": "510"})


def readFile(filename, chunk_size=512):
    """
    缓冲流下载文件方法
    :param filename:
    :param chunk_size:
    :return:
    """
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
# 取消上传的文件
def cancelfile(request):
    pass


# 查看文件信息(包括文件名,被下载次数,上传人,评论信息) 传过来一个资源id
def showfile(request):
    if request.method == "GET":
        resource_id = request.GET.get("id")
        res = Resource.objects.filter(id=resource_id).values("name", "download_count", "upload_user", "describe")
        res = list(res)
        filename = res[0]["name"]
        download_count = res[0]["download_count"]
        user_id = res[0]["upload_user"]
        user_name = list(Info.objects.filter(id=user_id).values("user_name"))[0]["user_name"]
        describe = res[0]["describe"]
        file = {
            "filename": filename,
            "download_count": download_count,
            "upload_user": user_name,
            "describe": describe
        }
        print(file)
        return JsonResponse({"file": file})


# 查看文件信息(包括文件名,被下载次数,上传人,评论信息)
def showmyupfile(request):
    try:
        if request.method == 'GET':
            qid = request.GET.get('id')
            qid = Resource.objects.filter(upload_user_id=qid).values('id', 'name', 'download_count', 'upload_time',
                                                                     'need_integral', 'describe')
            if qid:
                for i in qid:
                    i['upload_time'] = str(i['upload_time'])
                return HttpResponse(json.dumps(list(qid), ensure_ascii=False))
            else:

                return JsonResponse({"code": "518"})
    except Exception as ex:
        return JsonResponse({"code": "510"})


# 删除用户自己上传的文件
def delmyupfile(request):
    if request.method == 'POST':
        user_id = json.loads(request.body)['qid']
        user_index = json.loads(request.body)['qindex']
        res = Resource.objects.filter(upload_user_id=user_id)[user_index].delete()
        if res[0]:
            return JsonResponse({"code": "213"})
        else:
            return JsonResponse({"code": "510"})
    else:
        return JsonResponse({"code": "510"})


# 评论资源功能
def commentFile(request):
    pass

    def showfile(request):
        if request.method == "GET":
            resource_id = request.GET.get("id")
            res = Resource.objects.filter(id=resource_id).values("name", "download_count", "upload_user", "describe")
            res = list(res)
            filename = res[0]["name"]
            download_count = res[0]["download_count"]
            user_id = res[0]["upload_user"]
            user_name = list(Info.objects.filter(id=user_id).values("user_name"))[0]["user_name"]
            describe = res[0]["describe"]
            file = {
                "filename": filename,
                "download_count": download_count,
                "upload_user": user_name,
                "describe": describe
            }
            print(file)
            return JsonResponse({"file": file})


# 添加收藏 传过来用户的telephone和要收藏资源的id
def addCollect(request):
    if request.method == "GET":
        resource_id = request.GET.get('id')  # 被收藏资源的id
        tel = request.GET.get('telephone')  # 用户的电话号，要根据用户的电话号查到该用户的id
        user_id = list(User.objects.filter(telephone=tel).values("id"))[0]["id"]
        data = {
            "user_id": user_id,
            "resource_id": resource_id
        }
        print(data)
        res = Collect.objects.filter(user_id=user_id)
        if not res:
            Collect.objects.create(**data)  # 向Collect用户收藏表添加数据
            return JsonResponse({"code": "209"})  # 收藏成功
        else:
            return HttpResponse("已收藏过了")
    else:
        return JsonResponse({"code": "404"})



# 取消收藏
def cancelCollect(request):
    if request.method == "GET":
        tel = request.GET.get('telephone')  # 用户的电话号，要根据用户的电话号查到该用户的id
        user_id = list(User.objects.filter(telephone=tel).values("id"))[0]["id"]  # 用户id
        data = {
            "user_id": user_id,
        }
        res = Collect.objects.filter(user_id=user_id)
        print(data)
        if res:
            Collect.objects.filter(user_id=user_id).delete()  # 向Collect用户收藏表添加数据
            return JsonResponse({"code": "222"})  # 取消收藏成功
        else:
            return HttpResponse("还没有收藏呢")
    else:
        return JsonResponse({"code": "404"})


# 检测文件重复(根据标题) 传过来一个title
def detectionRepetition(request):
    if request.method == "GET":
        title = request.GET.get("title")
        res = Resource.objects.filter(title=title)
        if res:
            return HttpResponse("文件重复")
        else:
            return HttpResponse("文件不重复")


# 点赞
def like(request):
    if request.method == "GET":
        resource_id = request.GET.get('id')  # 资源的id
        like_num = Resource.objects.filter(id=resource_id).values("like_num")  # 查询结果为对象集合
        like_num = list(like_num)[0]["like_num"]  # 点赞数
        new_like_num = like_num + 1  # 点赞数+1
        print(resource_id, like_num, new_like_num)
        res = Resource.objects.filter(id=resource_id).update(like_num=new_like_num)  # 更新点赞数
        return JsonResponse({"like_num": new_like_num})  # 返回点赞数
    else:
        return JsonResponse({"code": "404"})


# 查看所有用户上传的文件
def showAllFile(request):
    res=list(Resource.objects.all().values())
    print(res)
    res=formDatatime(res)
    print(res)
    for i in range(len(res)):
        print(i)
        print(res[i])
        print(res[i]["upload_user_id"])
        res[i]["upload_user"]=list(Info.objects.filter(id=res[i]["upload_user_id"]).values())[0]["user_name"]
    print(res)
    return HttpResponse(json.dumps(res))