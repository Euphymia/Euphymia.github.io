# Opencv 载入图片和视频

---

> * opencv载入图片
> * 简介waitkey()函数
> * opencv载入视频
> * 保存照相机的内容到电脑

---

## opencv载入图片

```python
import cv2
#显示一张名为'b.png'的图片
#以RGB的格式读取
img = cv2.imread('b.jpg',cv2.IMREAD_COLOR)
#以灰度图像读取
# img = cv2.imread('b.png',cv2.IMREAD_GRAYSCALE)
#弱想将图片完整的显示出来，需要先设置一个窗口，并传入窗口的名字和0(表示全部显示)两个参数即可
cv2.namedWindow('img',0)
#查看图片的维度
# print(img.shape)
# >>> (1400, 1800, 3)
if img is None:
     print('Object is not exist')
else:
    pass
    #在设置好的名为'img'的窗口中显示
    cv2.imshow('img',img)
    #waitkey中的参数表示延迟，单位值ms，若为0表示停在这一贞，等待返回键盘输入值
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## 简介waitkey()函数

函数功能：

**waitKey()函数的功能是不断刷新图像，频率时间为delay，单位为ms。返回值为当前键盘按键值。**

所以显示图像时，如果需要在imshow(“xxxx”,image)后吐舌头加上while（cvWaitKey(n)==key）为大于等于0的数即可，那么程序将会停在显示函数处，不运行其他代码;直到键盘值为key的响应之后。

delay>0时，延迟”delay”ms，在显示视频时这个函数是有用的，用于设置在显示完一帧图像后程序等待”delay”ms再显示下一帧视频；如果使用waitKey(0)则只会显示第一帧视频。

返回值：如果delay>0,那么超过指定时间则返回-1；如果delay=0，将没有返回值。 
如果程序想响应某个按键，可利用if(waitKey(1)==Keyvalue)； 
如果delay<0,等待时间无限长，返回值为按键值

经常程序里面出现if( waitKey(10) >= 0 ) 是说10ms中按任意键进入此if块

## Opencv 载入视频

```python
import cv2
import numpy as np
#从摄像头读取视频信息
cam = cv2.VideoCapture(0)
#从本地文件读入视频信息
# capture = cv2.VideoCapture('test.avi')
while(True):
    tf,frame = cam.read()
    if tf ==True:
        #输出tf
        #将RGB图像转换成HSV图像
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #将RGB图像转换成灰度图
        # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #将图像的每个像素进行过滤(进过下面选取的最高最低值过滤)
        upper_red = np.array([130,255,255])
        lower_red = np.array([110,100,100])
        mask = cv2.inRange(frame,lower_red,upper_red)
        #添加mask
        frame = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('Single Frame',frame)
        key = cv2.waitKey(1)
        #ASC码27对应的键是Esc，按下Esc键即可退出视频显示
        if key == 27:
            #退出
            break
        elif key == ord('x'):
            print('you have preesed the letter X')
    else :
        print("could not read from camera...")        
        break
cam.release()
cv2.destroyAllWindows()
```

## Opencv 保存照相机的内容到电脑

```python
import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
#将摄像头录下的视频保存到电脑
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#VidioWriter的参数
#videoWriter = cv2.VideoWriter('out.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
#fps调为30时，跟实际帧数差不多
vid = cv2.VideoWriter('output.avi', fourcc, 30, (640,480))
t=time.time()
#只录制十秒
while(time.time()-t<10):
    tf, frame = cam.read()
    #print tf
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #写入电脑
    vid.write(frame)
    cv2.imshow('Single Frame', frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key
        break
    elif key == ord('x'):
        print ("You have pressed the letter X")

cam.release()
vid.release()
cv2.destroyAllWindows()
```

