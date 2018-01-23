# SVM多分类及K折交叉验证

---

> * 使用SVM对原始数据集及挑选出来的新数据集进行多分类
> * 使用K折交叉验证测试
> * 代码

---

## 代码

```python
'''
Created on 2018/1/23

@author Euphymia
'''
from numpy import *
import pandas as pd
from sklearn import cross_validation
from sklearn import svm
# import csv
#载入数据
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open("Tic-Tac-toe/Tic-Tac-toe.txt",'r')
    for line in fr.readlines():  
        lineArr = line.strip().split(',')
        #在前面加一个1.0是为了之后选取元素时直接使用第几个元素的位置而不考虑下标
        lineArr.insert(0,1.0)
        lineArr=array(lineArr)
        lineArr=lineArr.astype(float)

        dataMat.append(lineArr[:-1])
        labelMat.append(lineArr[-1])
        # i+=1
    return dataMat,labelMat
#获取数据集
dataMat,labelMat=loadDataSet()
#因为loadDataSet返回的数据集是列表类型的，现在再转为numpy
dataMat=array(dataMat)
newdataMat=dataMat[:,(5,9,1,7,3,6,4,2)]
print("数据维度",shape(dataMat))
#使用处理过的数据K折交叉验证 
clf=svm.SVC(kernel='linear',degree=3,C=1) 
scores= cross_validation.cross_val_score(clf,dataMat,labelMat,cv=10)
m1=mean(scores)
print("使用处理过的数据K折交叉验证:")
print(scores)
print("mean=",m1)
#使用挑选出来的特征数据K折交叉验证 
clf=svm.SVC(kernel='rbf',C=1)
scores= cross_validation.cross_val_score(clf,newdataMat,y=labelMat,cv=10)
m2=mean(scores)
print("使用挑选出来的特征数据K折交叉验证: ")
print(scores)
print("mean=",m2)
```

