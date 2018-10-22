# Author:raobaoshi
from datetime import datetime
print(isinstance(datetime.now(),datetime))

print(type(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))