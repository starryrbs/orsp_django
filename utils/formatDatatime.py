# Author:raobaoshi
from datetime import datetime
import time
def formDatatime(res):
    for item in range(len(res)):
        # print("item", item)
        for i in res[item].items():
            if isinstance(i[1], datetime):
                res[item][i[0]] = i[1].strftime("%Y-%m-%d %H:%M:%S")
    return res

def timestamp_from_objectid(objectid):
    ''' ObjectId convert timestamp '''
    result = 0
    try:
        result = time.mktime(objectid.generation_time.timetuple())  # get timestamp
    except:
        pass
    return result


import bson
# print(bson.objectid.ObjectId("5bb57eba923ce03158254d17").__str__())


