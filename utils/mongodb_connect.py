# Author:raobaoshi
from pymongo import MongoClient
conn = MongoClient('123.207.11.101', 27017)
db = conn.orsp  # 连接mydb数据库，没有则自动创建