# from django.test import TestCase
# from user.models import *
# Create your tests here.

def insertData():
    import json
    with open('../test/p_c.json','r',encoding='utf-8') as f:
        data=json.load(f)
        for i in data:
            # print(i["city"])
            for j in i["city"]:

                print(i["name"],j["name"])


insertData()
    #         print(i["name"])
    #         i={
    #             "province_name":i["name"]
    #         }
    #         Province.objects.create(**i)
    # return HttpResponse("成功")
