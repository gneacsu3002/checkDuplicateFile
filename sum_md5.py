#!/usr/bin/env python
import os
from hashlib import md5
from mmap import mmap, ACCESS_READ

def Memhash(path):
 if os.path.isfile(path) and not os.path.islink(path):
   sz = os.path.getsize(path)
   if sz > 0 :
    with open(path) as file, mmap(file.fileno(), 0, access=ACCESS_READ) as file:
      # print(md5(file).hexdigest())
      hs = md5(file).hexdigest()
   else:
      hs = "empty"
   with open("db.csv", "a") as f:
      f.write(os.path.basename(path) + '\t' + hs + '\t' + str(sz) + '\t' + str(os.path.getmtime(path)) + '\t' + path + '\n')

if __name__ == '__main__':
  cale = "."
  
  with open("db.csv", "w") as f:
    f.write("fileName" + '\t' + "MD5sum" + '\t' + "Size" + '\t' + "ModifTime" + '\t' + "Path" + '\n')
  
  for root, dirs, files in os.walk(cale):
    for filename in files:
      # print(os.path.join(root, filename))
      Memhash(os.path.join(root, filename))
