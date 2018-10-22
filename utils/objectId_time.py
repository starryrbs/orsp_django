# Author:raobaoshi

from bson.objectid import ObjectId
import datetime
import time

def general_obj_from_time(from_datetime=None, time_delta=None):
    if from_datetime is None or not isinstance(from_datetime, datetime.datetime):
        from_datetime = datetime.datetime.now()  # 时间元组
    if time_delta:  # time_delta 是datetime.timedelta 类型,可以进行时间的加减运算
        from_datetime = from_datetime + time_delta

    return ObjectId.from_datetime(from_datetime)


# print(obj)
# time2 = obj.generation_time.timetuple()
# print(time2)

import uuid
print(uuid.uuid4())