# 使用Opencv进行人脸识别

---

> * 使用opencv自带的人脸识别工具进行人脸识别
> * 识别视频中的人脸
> * 识别照片中的人脸

---

## 识别照片中的人脸

```python
识别照片人脸
import cv2
#获取照片
img = cv2.imread("a.jpg")
#new一个新窗口，用于显示照片，设置窗口大小为0，即可全部显示，避免照片过大显示不全的问题
cv2.namedWindow('img',0)
#载入训练好的人脸识别检测器
#经过测试，该检测器只对正脸的检测效果较好，侧脸很差
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#将RGB图像转换成灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#找到人脸的位置
#若找到返回一个描述人脸位置的矩阵，[x,y,w,h]分别是其实坐标的位置(x,y)，向右，向下的偏移量(w,h)
#若没找到则返回一个空元组
faces = face_csc.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    #画出识别的像框
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,200), 1)
#在img窗口中显示图片
cv2.imshow('img', img)
cv2.waitKey(0)
```



## 识别视频中的人脸

```python
#识别视频人脸
import cv2
import numpy as np
#获取照相机
cam = cv2.VideoCapture(0)
#也可以读取视频,在当前目录下必须存在nn.avi
#cam = cv2.VideoCapture('nn.avi')
#载入训练好的人脸识别检测器
#经过测试，该检测器只对正脸的检测效果较好，侧脸很差
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow('Single Frame',1)
while(True):
    #获取照相机图像
    tf, img = cam.read()
    #print tf
    # frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #将RGB图像转换成灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #找到人脸的位置
    #若找到返回一个描述人脸位置的矩阵，[x,y,w,h]分别是其实坐标的位置(x,y)，向右，向下的偏移量(w,h)
    #若没找到则返回一个空元组
    faces = face_csc.detectMultiScale(gray, 1.1, 4)
    # print(faces)
    # print(faces.shape)
    for (x, y, w, h) in faces:
        #画出识别的像框
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,200), 1) 
    #显示图像
    cv2.imshow('Single Frame', img)
    key = cv2.waitKey(1)
    if key == 27: #esc key
        break
    elif key == ord('x'):
        print ("You have pressed the letter X")

cam.release()
cv2.destroyAllWindows()
```



