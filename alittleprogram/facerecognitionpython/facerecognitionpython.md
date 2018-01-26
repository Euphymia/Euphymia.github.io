# 用python实现最简单的人脸识别

---

> * 1.主要调用的face_recognition包其实是使用的dlib包
> * 2.找到图片中的人脸
> * 3.画出照片中人脸的轮廓(68个点)
> * 4.给图片中找到的脸化妆
> * 5.识别相机中的人脸
> * 6.给相机中的人脸打上高斯模糊
> * 7.识别出视频中的人脸并输出保存在一个新的视频文件中

---

## 1.dlib包

dlib是一个c++的库，其中包括人脸识别的方法。

使用训练好的人脸检测器，shape_predictor_68_face_landmarks.dat(与opencv类似)

可以检测出人脸的位置，用68个点描述出来。

## 代码

```python
import cv2  
import dlib  
import numpy  
import sys  
  
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"  
  
  
#1.使用dlib自带的frontal_face_detector作为我们的人脸提取器  
detector = dlib.get_frontal_face_detector()  
  
#2.使用官方提供的模型构建特征提取器  
predictor = dlib.shape_predictor(PREDICTOR_PATH)  
  
class NoFaces(Exception):  
    pass  
im=cv2.imread("32bit.png",cv2.IMREAD_COLOR)
#3.使用detector进行人脸检测 rects为返回的结果  
rects = detector(im,1)  
print(rects[0])
print(predictor(im,rects[0]))
#4.输出人脸数，dets的元素个数即为脸的个数  
if len(rects) >= 1: 

    print("{} faces detected".format(len(rects)))  
      
if len(rects) == 0:  
    raise NoFaces  
  
for i in range(len(rects)):
      
    #5.使用predictor进行人脸关键点识别  
    landmarks = numpy.matrix([[p.x,p.y] for p in predictor(im,rects[i]).parts()])  
    print(len(landmarks))
    im = im.copy()  
  
    #使用enumerate 函数遍历序列中的元素以及它们的下标  
    for idx,point in enumerate(landmarks):  
        pos = (point[0,0],point[0,1])  
        #cv2.putText(im,str(idx),pos,  
                    #fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  
                    #fontScale=0.4,  
  
                    #color=(0,0,255))  
        #6.绘制特征点  
        cv2.circle(im,pos,3,color=(0,255,0))  
          
cv2.namedWindow("im",2)  
cv2.imshow("im",im)  
cv2.waitKey(0) 
```

结果如下图所示：

![dlibresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\dlibresult.PNG)

## 2.找到图片中的人脸

这里直接调用face_locations函数找到人脸的位置(返回一个四元组用来描述矩形人脸位置)

```python
from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
#>>>I found 1 face(s) in this photograph.
for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
#>>>A face is located at pixel location Top: 241, Left: 419, Bottom: 562, Right: 740
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
```

已将人脸单独显示出来，结果如下：

![findfaceresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\findfaceresult.PNG)

## 3.画出照片中人脸的轮廓(68个点)

其实就是利用dlib函数找到68个点，然后选择各个部位的点用线连接起来

```python
from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)


print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    facial_features = [
        'chin',
        'left_eyebrow',
        'right_eyebrow',
        'nose_bridge',
        'nose_tip',
        'left_eye',
        'right_eye',
        'top_lip',
        'bottom_lip'
    ]

    for facial_feature in facial_features:
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for facial_feature in facial_features:
        d.line(face_landmarks[facial_feature], width=5)

    pil_image.show()

```

画出的轮廓如下图所示：

![lunkuoresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\lunkuoresult.PNG)

## 4.给图片中找到的脸化妆

这里是先找出的68个点，然后对各个部位进行改造。

给眉毛上色，嘴唇上色，眼睛变亮，延长眼线。

```python
from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

    pil_image.show()

```

化妆的结果如下：

![makeupresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\makeupresult.PNG)

## 5.识别相机中的人脸

主要思想：先预先保存想要识别出的人脸的照片以及对应的名字。调用cv2，对相机中每一帧图像进行识别，找出人脸并与预设的人脸库做比较，如果出现相近的就在人脸框中显示出对应的名字。

1.为了加速识别，对每一帧图像进行缩放，缩小4倍(最后在恢复)

2.这里对比人脸相似度用的是face_recognition自带的compare_face函数，其实就是简单的利用numpy的计算范数距离的方法(这里使用默认的二范数)。两张图片的距离小于0.6时，认为是同一个人。

```python
import face_recognition
import cv2

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
xuhao_image = face_recognition.load_image_file("xuhao.jpg")
xuhao_face_encoding = face_recognition.face_encodings(xuhao_image)[0]
known_faces = [
    obama_face_encoding,
    xuhao_face_encoding
]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #当视频一直存在时 ret一直为True
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            if match[0]:
                name = "Barack"
            elif match[1]:
                name = "xuhao"
                
            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1)==27:
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

```

识别结果如下所示：

![xuhaoresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\xuhaoresult.PNG)

## 6.给相机中的人脸打上高斯模糊

主要思想：

对识别出人脸的区域调用cv2.GaussianBlur函数高斯模糊化

同样先对每一帧图片缩小4倍，最后在放大

```python
import face_recognition
import cv2

# This is a demo of blurring faces in video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top:bottom, left:right]

        # Blur the face image
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        # Put the blurred face region back into the frame image
        frame[top:bottom, left:right] = face_image

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
```

高斯模糊结果如下所示：

![blurresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\blurresult.PNG)

## 7.识别出视频中的人脸并输出保存在一个新的视频文件中

主要思想：

识别出视频中的人脸并将它保存再一个新的视频里。

```python
import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("hamilton_clip.mp4")

length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))

# Load some sample pictures and learn how to recognize them.
lmm_image = face_recognition.load_image_file("lin-manuel-miranda.png")
lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]

al_image = face_recognition.load_image_file("alex-lacamoire.png")
al_face_encoding = face_recognition.face_encodings(al_image)[0]

known_faces = [
    lmm_face_encoding,
    al_face_encoding
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Lin-Manuel Miranda"
        elif match[1]:
            name = "Alex Lacamoire"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)
    cv2.imshow('output.avi',frame)
    key = cv2.waitKey(1)
    #ASC码27对应的键是Esc，按下Esc键即可退出视频显示
    if key == 27:
    #退出
        break
    elif key == ord('x'):
        print('you have preesed the letter X')
# All done!
input_movie.release()
cv2.destroyAllWindows()
```

结果如下所示：

![vidiooutputresult](C:\Users\think\Documents\GitHub\Euphymia.github.io\alittleprogram\facerecognitionpython\vidiooutputresult.PNG)