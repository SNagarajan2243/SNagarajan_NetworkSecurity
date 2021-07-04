import hashlib

import bcrypt

salt=bcrypt.gensalt()

password=input("Enter your password: ")

hashing=bcrypt.hashpw(password.encode(),salt)

hashing=hashing+salt

print(hashing)
