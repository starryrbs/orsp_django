# Author:raobaoshi
from werkzeug.security import generate_password_hash,check_password_hash
password="111111111"
aa=generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
print("aa"+aa)
password1="222222222"
aaa=generate_password_hash(password1, method='pbkdf2:sha1:2000', salt_length=8)
print("aaa"+aaa)

print(check_password_hash(aa,password))
print(check_password_hash(aaa,password))