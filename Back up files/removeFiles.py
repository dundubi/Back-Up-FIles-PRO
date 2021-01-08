import os
import shutil
import time
yearDay = time.localtime().tm_mday
path = "C:/Users/Dundubi Raaj/Downloads"
seconds = time.time()
print(seconds)
print(time.ctime(seconds))
if os.path.exists(path) :
    Folder_Generator = os.walk(path)
    print(Folder_Generator)