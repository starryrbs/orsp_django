# Author:raobaoshi
import datetime
import time
from pymongo import MongoClient
conn = MongoClient('123.207.11.101', 27017)
db = conn.orsp  # 连接mydb数据库，没有则自动创建
db.authenticate('orsp','123456')
from bson import ObjectId
# res=list(db.order.update({"_id":ObjectId("5bcd6912923ce015f8e938c9")},{'$set':{"sellerSelectGood.status":1}}))
# print(res)

def object_id_from_datetime(from_datetime=None):
    ''' According to the time manually generated an ObjectId '''
    if not from_datetime:
        from_datetime = datetime.datetime.now()
    return ObjectId.from_datetime(generation_time=from_datetime)
# print(object_id_from_datetime(from_datetime=1538609282))


