import hashlib

password=input("Enter your password: ")

#password="pa$$w0rd"
temporary_password=hashlib.md5(password.encode())

print(temporary_password.hexdigest())
