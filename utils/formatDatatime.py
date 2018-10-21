# Author:raobaoshi
from datetime import datetime
def formDatatime(res):
    for item in range(len(res)):
        print("iten", item)
        for i in res[item].items():
            if isinstance(i[1], datetime):
                res[item][i[0]] = i[1].strftime("%Y-%m-%d %H:%M:%S")
    return res