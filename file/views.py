from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from orsp_django import settings
import uuid
from file.models import *
from user.models import *
import json
from django.http import FileResponse
from utils.formatDatatime import *
import jwt

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
    data = json.loads(request.body)
    # try:
    #     resourceTypeId_id = list(ResourceType.objects.filter(name=data["name"]).values())[0]["id"]
    #     data["resourceTypeId_id"] = resourceTypeId_id
    #     resourceTypeId_id = list(ResourceType.objects.filter(name=data["resourceType"]).values())[0]["id"]
    #     data["resourceTypeId_id"] = resourceTypeId_id
    # except Exception as ex:
    #     print(ex)
    #     data["resourceTypeId_id"]=1
    # del data["resourceType"]
    data["share_num"] = 0
    data["like_num"] = 0
    # print(data)
    res=Resource.objects.filter(title=data["title"]).values()
    if res:
        return HttpResponse("已成功上传")
    else:
        integral = Info.objects.filter(id=data["upload_user_id"]).values("integral")[0]["integral"]
        new_integral = int(integral) + 1
        Info.objects.filter(id=data["upload_user_id"]).update(integral=new_integral)
        Resource.objects.create(**data)
        return HttpResponse("上传成功,获得1积分")


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


# 判断是否已下载
def whetherdownload(request):
    print("===================")
    if request.method == "POST":
        filename = json.loads(request.body)
        print(filename)
        if filename['fname']:
            print(filename['fname'])
            file=Resource.objects.filter(name=filename["fname"]).values("id","need_integral")[0]
            userid=filename["userid"]
            res=Download.objects.filter(user=userid,file=file["id"])
            if res:
                return JsonResponse({"code":"220"}) # 已下载
            else:
                return JsonResponse({"code":"420"})
    else:
        return JsonResponse({"code":"404"})

# 下载文件
def downloadfile(request):
    if request.method == "POST":
        filename = json.loads(request.body)
        print(filename)
        if filename['fname']:
            print(filename['fname'])
            file=Resource.objects.filter(name=filename["fname"]).values("id","need_integral")[0]
            # file_id=file["id"]
            # print(11111,file_id)
            need_integral=file["need_integral"]
            # media / pic
            filepath = ('media/pic/{0}'.format(filename['fname']))
            response = FileResponse(readFile(filepath))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename['fname'])
            userid=filename["userid"]
            res=Download.objects.filter(user=userid,file=file["id"])
            # 没有该下载记录
            if not res:
                integral=Info.objects.filter(id=userid).values("integral")[0]["integral"]
                new_integral=int(integral)-int(need_integral)
                print(new_integral)
                Info.objects.filter(id=userid).update(integral=new_integral) # 扣掉积分
                dd={
                    "file_id":file["id"],
                    "user_id":filename["userid"]
                }
                Download.objects.create(**dd)
                # Download.objects# 保存下载记录，以后下载不要钱
                return response
            else:
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
        res = Resource.objects.filter(id=resource_id).values("name", "download_count", "upload_user", "describe","title")
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
    else:
        return JsonResponse({"code": "404"})

# 查看已下载的文件
def showDownloadFile(request):
    if request.method=="POST":
        try:
            userid=json.loads(request.body)["userid"]
            print(userid)
            uploadcount = Resource.objects.filter(upload_user=userid).count()  # 我上传文件的次数
            downloadcount = Download.objects.filter(user=userid).count()  # 我下载文件的次数
            fileid=list(Download.objects.filter(user=userid).values("file"))  # 我下载的文件id
            print(fileid)
            uu=[]
            for i in range(len(fileid)):
                mes=Resource.objects.filter(id=fileid[i]["file"]).values("title","describe","upload_time","need_integral","upload_user","like_num","share_num","id")[0]
                collectcount = Collect.objects.filter(resource=fileid[i]["file"]).count()
                print(collectcount,22222)
                mes["collectcount"]=collectcount
                upload_time=mes["upload_time"].strftime("%Y-%m-%d %H:%M:%S")
                mes["upload_time"]=upload_time
                upload_user_name=Info.objects.filter(id=mes["upload_user"]).values("user_name")[0]["user_name"]  # 被下载文件的上传者
                mes["upload_user_name"]=upload_user_name
                uu.append(mes)
            print(uu)
            cc={
                "uploadcount":uploadcount,
                "downloadcount":downloadcount
            }
            uu.append(cc)
            return HttpResponse(json.dumps(uu,ensure_ascii=False))
        except Exception as e:
            print(e)
    else:
        return JsonResponse({"code":"404"})


# 查看我发布的资源 (另一个注意别删)
def getMyUploadFile(request):
    if request.method=="POST":
        try:
            userid=json.loads(request.body)["userid"]
            print(userid)
            uploadcount = Resource.objects.filter(upload_user=userid).count()  # 我上传文件的次数
            downloadcount = Download.objects.filter(user=userid).count()  # 我下载文件的次数
            fileid=list(Resource.objects.filter(upload_user_id=userid).values())  # 我上传的文件
            print(fileid)
            uu=[]
            for i in range(len(fileid)):
                collectcount = Collect.objects.filter(resource_id=fileid[i]["id"]).count()
                fileid[i]["collectcount"]=collectcount
                upload_time=fileid[i]["upload_time"].strftime("%Y-%m-%d %H:%M:%S")
                fileid[i]["upload_time"]=upload_time
                upload_user_name=Info.objects.filter(id=fileid[i]["upload_user_id"]).values("user_name")[0]["user_name"]  # 被下载文件的上传者
                fileid[i]["upload_user_name"]=upload_user_name
                uu.append(fileid[i])
            cc={
                "uploadcount":uploadcount,
                "downloadcount":downloadcount
            }
            uu.append(cc)
            return HttpResponse(json.dumps(uu,ensure_ascii=False))
        except Exception as e:
            print(e)
    else:
        return JsonResponse({"code":"404"})



# 已收藏文件
def showCollectFile(request,id):
    if request.method=="GET":
        list_file=Collect.objects.filter(user_id=id).values("resource_id")
        uploadcount = Resource.objects.filter(upload_user=id).count()  # 我上传文件的次数
        downloadcount = Download.objects.filter(user=id).count()  # 我下载文件的次数
        file=[]
        for i in list_file:
            print("i",i)
            collectcount = Collect.objects.filter(resource=i["resource_id"]).count()
            uu=Resource.objects.filter(id=i["resource_id"]).values()[0]
            uu["upload_time"]=uu["upload_time"].strftime("%Y-%m-%d %H:%M:%S")
            upload_user_name=Info.objects.filter(id=uu["upload_user_id"]).values("user_name")[0]["user_name"]
            uu["upload_user_name"]=upload_user_name
            uu["collectcount"] = collectcount
            file.append(uu)
        cc = {
            "uploadcount": uploadcount,
            "downloadcount": downloadcount
        }
        file.append(cc)
        print(file)
        return HttpResponse(json.dumps(file,ensure_ascii=False))


# 查看我的文件信息(包括文件名,被下载次数,上传人,评论信息)
def showmyupfile(request):
    try:
        if request.method == 'GET':
            qid = request.GET.get('id')
            qid = Resource.objects.filter(upload_user_id=qid).values('id', 'name', 'download_count', 'upload_time','need_integral','title','describe')
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
    else:
        return JsonResponse({"code": "404"})


# 添加收藏 传过来用户的telephone和要收藏资源的id
def addCollect(request):
    if request.method == "POST":
        res=json.loads(request.body)
        resource_id = res["id"]  # 被收藏资源的id
        userid = res["userid"]  # 收藏人id
        data = {
            "user_id": userid,
            "resource_id": resource_id
        }
        print(data)
        res = Collect.objects.filter(user_id=userid,resource_id=resource_id)
        if not res:
            Collect.objects.create(**data)  # 向Collect用户收藏表添加数据
            return JsonResponse({"code": "209"})  # 收藏成功
        else:
            return HttpResponse("已收藏过了")
    else:
        return JsonResponse({"code": "404"})


# 取消收藏
def cancelCollect(request):
    if request.method == "POST":
        res = json.loads(request.body)
        resource_id = res["id"]  # 被收藏资源的id
        userid = res["userid"]  # 收藏人id
        data = {
            "userid": userid,
        }
        res = Collect.objects.filter(user_id=userid)
        print(data)
        if res:
            Collect.objects.filter(user_id=userid,resource_id=resource_id).delete()
            return JsonResponse({"code": "222"})  # 取消收藏成功
        else:
            return HttpResponse("还没有收藏呢")
    else:
        return JsonResponse({"code": "404"})


# 收藏人数
def collectnumber(request):
    if request.method == "POST":
        try:
            id=json.loads(request.body)["id"]
            print(id,88)
            collectcount=Collect.objects.filter(resource=id).count()
            print(collectcount,888)
            return HttpResponse(str(collectcount))
        except Exception as e:
            print(e)
    else:
        return JsonResponse({"code":"404"})


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
        res[i]["upload_user"]=list(Info.objects.filter(id=res[i]["upload_user_id"]).values())[0]["user_name"]
        res[i]["collectcount"] = Collect.objects.filter(resource=res[i]["id"]).count()
    print(666666666,res)
    return HttpResponse(json.dumps(res))

# 通过二级路由查所有文件
def showFileByCondition(request):
    if request.method=="POST":
        print(1111111111111111111)
        twofieldid=json.loads(request.body)["twofieldid"]
        # print(condition)
        # txtcondition=condition["txtcondition"]
        # print("txtcondition",txtcondition)
        # twofieldid=condition["twofieldid"]
        # print("twofieldid",twofieldid)
        # resoursetypeid=condition["resoursetypeid"]
        # print("resoursetypeid",resoursetypeid)
        # twoTechnicalFieldId=json.loads(request.body)["twoFieldId"]
        # file=None
        # if txtcondition and not twofieldid and not resoursetypeid:
        #     file = list(Resource.objects.filter(title__icontains=txtcondition).values())
        #
        #
        # elif txtcondition and twofieldid and not resoursetypeid:
        #     file_1 = list(Resource.objects.filter(title__icontains=txtcondition).values())
        #     file=[]
        #     for i in range(len(file_1)):
        #         if file_1[i]["twoTechnicalFieldId_id"]==twofieldid:
        #             file.append(file_1[i])
        #
        #
        # elif txtcondition and not twofieldid and resoursetypeid:
        #     file_1 = list(Resource.objects.filter(title__icontains=txtcondition).values())
        #     file=[]
        #     for i in range(len(file_1)):
        #         if file_1[i]["resourceTypeId_id"]==twofieldid:
        #             file.append(file_1[i])
        #
        #
        # elif txtcondition and twofieldid and resoursetypeid:
        #     file_1 = list(Resource.objects.filter(title__icontains=txtcondition).values())
        #     file = []
        #     for i in range(len(file_1)):
        #         if file_1[i]["twoTechnicalFieldId_id"] == twofieldid and file_1[i]["resourceTypeId_id"]==resoursetypeid:
        #             file.append(file_1[i])
        #
        #
        #
        # # not txtcondition and not resoursetypeid and twofieldid
        # else:
        #     # Resource.objects.filter(twoTechnicalFieldId_id=twofieldid).values()
        #     file=list(Resource.objects.filter(twoTechnicalFieldId_id=twofieldid).values())
        file = list(Resource.objects.filter(twoTechnicalFieldId_id=twofieldid).values())
        file = formDatatime(file)
        for i in range(len(file)):
            file[i]["user_name"]=Info.objects.filter(id=file[i]["upload_user_id"]).values()[0]["user_name"]
        print(1,file)
        return HttpResponse(json.dumps(file))



# 一级技术领域
def getTechnicalField(request):
    data=list(TechnicalField.objects.all().values())
    print(data)
    return HttpResponse(json.dumps(data))

# 二级技术领域
def getTwoTechnicalField(request):
    technicalFieldId=request.GET.get("id")
    data=list(TwoTechnicalField.objects.filter(technicalFieldId=technicalFieldId).values())
    # data=list(TwoTechnicalField.objects.all().values())
    print(data)
    return HttpResponse(json.dumps(data))


# 资源类型
def getResourceType(request):
    data=list(ResourceType.objects.all().values())
    print(data)
    return HttpResponse(json.dumps(data))


# 获得技术领域二级联动
def getAllTechnicalField(request):
    data=[]
    technicalField=list(TechnicalField.objects.all().values())
    for i in range(len(technicalField)):
        # print("技术领域一级标签",technicalField[i]["id"])
        data.append(technicalField[i])
        twoTechnicalField=list(TwoTechnicalField.objects.filter(technicalFieldId=technicalField[i]["id"]).values())
        data[i]["twoTechnicalField"]=twoTechnicalField
    # print(data)
    return HttpResponse(json.dumps(data))





