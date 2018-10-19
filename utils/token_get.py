# Author:raobaoshi

from functools import wraps
import jwt
import datetime
from flask import Blueprint, request

SECRECT_KEY="orsp"
def jwtEncoding(some, aud='webkit'):
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(hours=180)
    print(datetimeInt)
    option = {
        'iss': 'jobapp.com',
        'exp': datetimeInt,
        'aud': 'webkit',
        'some': some
    }
    encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256')
    # print(encoded2.decode())
    return encoded2.decode()

# token=jwtEncoding({"name":123})


# decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])

# print("decoded",decoded)