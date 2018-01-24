# 视频挂件

---

> * 使用Opencv完成视频挂件的功能

---

主要思想就是，先识别出面部的位置，再将所需的表情(图片)覆盖到识别的面部区域上，其中表情要做缩放处理(根据识别的面部矩形大小)。

## 代码

```python
import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import numpy as np
#面部检测工具包的路径(这里就在代码目录下)
cascPath = "haarcascade_frontalface_default.xml"  # for face detection
#获取面部检测工工具
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
anterior = 0
#加载将要用到的面部挂件(照片)
mst = cv2.imread('moustache.png')
hat = cv2.imread('cowboy_hat.png')
dog = cv2.imread('dog_filter.png')
#添加胡子的函数
def put_moustache(mst,fc,x,y,w,h):
    face_width = w
    face_height = h
    #控制胡子的大小(远近缩放)，等于面部识别的矩形的宽的0.41倍，长的0.14倍
    mst_width = int(face_width*0.4166666)
    mst_height = int(face_height*0.142857)
    mst = cv2.resize(mst,(mst_width,mst_height))
    #将照片覆盖在矩形框的指定位置    
    for i in range(int(0.62857142857*face_height),int(0.62857142857*face_height)+mst_height):
        for j in range(int(0.29166666666*face_width),int(0.29166666666*face_width)+mst_width):
            for k in range(3):
              #小于235，是除去照片中黑色的部分
                if mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k] <235:
                    fc[y+i][x+j][k] = mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k]
    #返回处理后的照片
    return fc
#添加帽子的函数
def put_hat(hat,fc,x,y,w,h):
    face_width = w
    face_height = h
    hat_width = face_width+1
    hat_height = int(0.35*face_height)+1
    hat = cv2.resize(hat,(hat_width,hat_height))
    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k]<235:
                    fc[y+i-int(0.25*face_height)][x+j][k] = hat[i][j][k]
    return fc
#添加狗挂件的函数
def put_dog_filter(dog,fc,x,y,w,h):
    face_width = w
    face_height = h
    
    dog = cv2.resize(dog,(int(face_width*1.5),int(face_height*1.75)))
    for i in range(int(face_height*1.75)):
        for j in range(int(face_width*1.5)):
            for k in range(3):
                if dog[i][j][k]<235:
                    fc[y+i-int(0.375*h)-1][x+j-int(0.25*w)][k] = dog[i][j][k]
    return fc
#根据选择调用不同的添加挂件的函数
print ("Select Filter:1.) Hat 2.) Moustache 3.) Hat and Moustache 4.) Dog Filter")
ch = int(input())
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #先将此刻的照片转为灰度图，在调用面部识别的方法，找到脸的位置
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
    # Draw a rectangle around the faces
    #给所有识别出来的面部加上挂件
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.putText(frame,"Person Detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        if ch==2:
            frame = put_moustache(mst,frame,x,y,w,h)
        elif ch==1:
            frame = put_hat(hat,frame,x,y,w,h)
        elif ch==3:
            frame = put_moustache(mst,frame,x,y,w,h)
            frame = put_hat(hat,frame,x,y,w,h)
        else:
            frame = put_dog_filter(dog,frame,x,y,w,h)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    #如果键盘输入为'Esc'则退出
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
```

