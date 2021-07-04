import hashlib

password=input("Enter your password: ")

#password="cool"

#temporary_password1=hashlib.shake_128(password.encode())

temporary_password1=hashlib.blake2s(password.encode())

temporary_password2=hashlib.sha3_512(password.encode())

temporary_password3=hashlib.sha512(password.encode())

temporary_password4=hashlib.sha384(password.encode())
#
# print("First hashing password: ")
#
# print("\n")
#
# print(temporary_password1.hexdigest())
#
# print("\n")

print("First hashing password: ")

print("\n")

print(temporary_password1.hexdigest())

print("\n")

print("Second hashing password: ")

print("\n")

print(temporary_password2.hexdigest())

print("\n")

print("Third hashing password: ")

print("\n")

print(temporary_password3.hexdigest())

print("\n")

print("Fourth hashing password: ")

print("\n")

print(temporary_password4.hexdigest())
