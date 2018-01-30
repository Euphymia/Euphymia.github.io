# glob函数及join和os.path.join的区别

---

> * glob函数
> * Python中join函数和os.path.join用法
> * os.path.splitext函数 

---

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

## os.path.splitext函数

分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作

```python
>>> os.path.splitext('c:\\csv\\test.csv') 
('c:\\csv\\test', '.csv')
```

