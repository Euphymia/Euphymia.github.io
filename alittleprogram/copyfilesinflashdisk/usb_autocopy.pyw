# 问题：
# 在后台运行一个可以copy插入u盘所有文件的程序
from time import sleep
import time
import os
import shutil
import re

def convert_bytes(num):
    #   this function will convert bytes to MB.... GB... etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return size
    except Exception as err:
        print(err)


def isUsbInsert():
    path = ""
    if (os.path.exists("G:") == True):
        path = "G:"
    return path

while True:
    usb_path = ""
    copy_path="E:\\copy"
    while True:
        usb_path = isUsbInsert()
        if usb_path == "":
            sleep(3)
        else:
            break
    # 使用shu.rmtree删除已有的copy的所有文件
    # if os.path.exists(copy_path):
    #     shutil.rmtree(copy_path)
    #创建一个保存文件的路径
    #为保证保存每次插入u盘的文件，根据时间的不同创建不同的文件夹
    nowtime=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    copy_path=copy_path+"\\"+nowtime
    os.makedirs(copy_path)
    for root, dirs, files in os.walk(usb_path):
        # for name in files:
        #     print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
        for name in files:
            file = os.path.join(root, name)
            if os.path.getsize(file) < 50*1024*1024:
                tfile = open(copy_path+"\\"+name, 'w')
                tfile.close()
                print(copy_path+"\\"+name)
                shutil.copy2(file, copy_path+"\\"+name)
    while os.path.exists("G:") == True:
        sleep(3)
        

