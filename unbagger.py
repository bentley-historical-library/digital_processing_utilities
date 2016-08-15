import os
import shutil

path_to_bag = raw_input("path/to/bag: ")

tags = [
    "bagit.txt",
    "manifest-md5.txt",
    "tagmanifest-md5.txt",
    "bag-info.txt"
]

for tag in tags:
    os.remove(os.path.join(path_to_bag, tag))
    
payload = os.path.join(path_to_bag, "data")

for name in os.listdir(payload):
    shutil.move(os.path.join(payload, name), path_to_bag)
    
os.rmdir(payload)
