# Author:raobaoshi
from werkzeug.security import generate_password_hash,check_password_hash
password="111111111"
aa=generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
print(aa)

print(check_password_hash(aa,password))