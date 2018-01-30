#用Python进行验证码识别

---

> * 主要思路
> * glob函数
> * Python中join函数和os.path.join用法
> * enumerate函数
> * os.path.splitext函数 
> * cv2.findContours函数
> * imutils python有什么用
> * python numpy.expand_dims的用法
> * Sklearn-train_test_split随机划分训练集和测试集
> * 标签二值化LabelBinarizer
> * python数据持久存储：pickle模块的基本使用
> * 代码见目录(附训练用的验证码)

---

## 主要思路

1. 从已有的验证码中抽取出单个数字或字母的图片及标签，作为训练集, 运行extract_single_letters_from_captchas.py
2. 使用图片训练卷积神经网络，运行train_model.py
3. 使用训练好的网络识别验证码，运行solve_captchas_with_model.py

## glob函数

glob模块是最简单的模块之一，内容非常少。用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。查找文件只用到三个匹配符：”*”, “?”, “[]”。”*”匹配0个或多个字符；”?”匹配单个字符；”[]”匹配指定范围内的字符，如：[0-9]匹配数字。

glob.glob()介绍

返回所有匹配的文件路径列表。它只有一个参数pathname，定义了文件路径匹配规则，这里可以是绝对路径，也可以是相对路径。下面是使用glob.glob的例子：

```python
import glob
#获取指定目录下的所有图片
print glob.glob(r"E:/Picture/*/*.jpg")
#获取上级目录的所有.py文件
print glob.glob(r'../*.py') #相对路径
```

## Python中join函数和os.path.join用法

Python中有join和os.path.join()两个函数，具体作用如下：

join：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
os.path.join()：  将多个路径组合后返回

一、函数说明

1.join（）函数

语法：‘sep’.join（seq）

参数说明：

sep：分隔符。可以为空

seq：要连接的元素序列、字符串、元组、字典等

上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

返回值：返回一个以分隔符sep连接各个元素后生成的字符串

2、os.path.join()函数

语法：  os.path.join(path1[,path2[,......]])

返回值：将多个路径组合后返回

注：第一个绝对路径之前的参数将被忽略

二、实例

```python
#对序列进行操作（分别使用' '与':'作为分隔符）
 
>>> seq1 = ['hello','good','boy','doiido']
>>> print ' '.join(seq1)
hello good boy doiido
>>> print ':'.join(seq1)
hello:good:boy:doiido
 
 
#对字符串进行操作
 
>>> seq2 = "hello good boy doiido"
>>> print ':'.join(seq2)
h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o
 
 
#对元组进行操作
 
>>> seq3 = ('hello','good','boy','doiido')
>>> print ':'.join(seq3)
hello:good:boy:doiido
 
 
#对字典进行操作
 
>>> seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
>>> print ':'.join(seq4)
boy:good:doiido:hello
 
 
#合并目录
 
>>> import os
>>> os.path.join('/hello/','good/boy/','doiido')
'/hello/good/boy/doiido'
```

## enumerate函数

- enumerate()是python的内置函数

- enumerate在字典上是枚举、列举的意思

- 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值

- enumerate多用于在for循环中得到计数

  - enumerate()返回的是一个enumerate对象

- 例如对于一个seq，得到:

  ```python
  (0, seq[0]), (1, seq[1]), (2, seq[2])
  ```

##os.path.splitext函数 

分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作

```python
>>> os.path.splitext('c:\\csv\\test.csv') 
('c:\\csv\\test', '.csv')
```

## cv2.findContours函数

**功能**：

找到图像的轮廓（连续的像素点）

需要注意的是cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的，再转成二值图

**参数**

第一个参数是寻找轮廓的图像；

第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
​    cv2.RETR_EXTERNAL表示只检测外轮廓
​    cv2.RETR_LIST检测的轮廓不建立等级关系
​    cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
​    cv2.RETR_TREE建立一个等级树结构的轮廓。

第三个参数method为轮廓的近似办法
​    cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
​    cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
​    cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法

**返回值：**

cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。

cv2.findContours()函数首先返回一个list，list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示。

```python
import cv2  
  
img = cv2.imread('D:\\test\\contour.jpg')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
  
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(img,contours,-1,(0,0,255),3)  
  
cv2.imshow("img", img)  
cv2.waitKey(0)  
```

##imutils python有什么用

提供一系列便捷功能进行基本的图像处理功能，如平移，旋转，缩放，骨架，matplotlib图像显示，排序的轮廓，边缘检测，让你更容易使用OpenCV和Python。

##python numpy.expand_dims的用法

expand_dims(a, axis)就是在axis的那一个轴上把数据加上去，这个数据在axis这个轴的0位置。 

例如原本为一维的2个数据，axis=0，则shape变为(1,2),axis=1则shape变为(2,1) 

再例如 原本为 (2,3),axis=0，则shape变为(1,2,3),axis=1则shape变为(2,1,3)

##Sklearn-train_test_split随机划分训练集和测试集

参数解释：

train_data：所要划分的样本特征集

train_target：所要划分的样本结果

test_size：样本占比，如果是整数的话就是样本的数量

random_state：是随机数的种子。

随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。

随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：

种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。

##标签二值化LabelBinarizer

对于标称型数据来说，preprocessing.LabelBinarizer是一个很好用的工具。比如可以把yes和no转化为0和1，或是把incident和normal转化为0和1。当然，对于两类以上的标签也是适用的。这里举一个简单的例子，说明将标签二值化以及其逆过程。

```python
# -*- coding: UTF-8 -*-
from sklearn import preprocessing
from sklearn import tree

# help(preprocessing.LabelBinarizer)#取消注释可以查看详细用法

# 特征矩阵
featureList=[[1,0],[1,1],[0,0],[0,1]]
# 标签矩阵
labelList=['yes', 'no', 'no', 'yes']
# 将标签矩阵二值化
lb = preprocessing.LabelBinarizer()
dummY=lb.fit_transform(labelList)
# print(dummY)
# 模型建立和训练
clf = tree.DecisionTreeClassifier()
clf = clf.fit(featureList, dummY)
p=clf.predict([[0,1]])
# print(p)#取消注释可以查看p的值

# 逆过程
yesORno=lb.inverse_transform(p)
print(yesORno)
```

## python数据持久存储：pickle模块的基本使用

python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

　　基本接口：

　　pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
　　file：对象保存到的类文件对象。file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的。

　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。

```python
#使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
```

