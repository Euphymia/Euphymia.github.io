# K-近邻算法

标签（空格分隔）： 机器学习

---

> * 心得
> * K-近邻算法代码
> * 撰写发布技术文稿（代码支持）
> * 撰写发布学术论文（LaTeX 公式支持）  

---
## 心得

    K-近邻算法不需要预先建立分类器，而是直接将结构化的待测试数据与已有的相同结构的“训练数据”对比，统计与待测试数据最相近（最小欧式距离）的前K个数据，选取K个数据中相同标签最多的标签作为待测试数据的标签。


##K-近邻算法代码
```python
from numpy import *
import operator
from os import listdir

def classify0(inX, dataSet, labels, k):
    dataSetSize=dataSet.shape[0]   #shape读取数据矩阵第一维度的长度
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  #tile重复数组inX，有dataSet行 1个dataSet列，减法计算差值
    sqDiffMat=diffMat**2 #**是幂运算的意思，这里用的欧式距离
    sqDisttances=sqDiffMat.sum(axis=1) #普通sum默认参数为axis=0为普通相加，axis=1为一行的行向量相加
    distances=sqDisttances**0.5
    sortedDistIndicies=distances.argsort() #argsort返回数值从小到大的索引值（数组索引0,1,2,3）
 #选择距离最小的k个点
    classCount={}
	
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]] #根据排序结果的索引值返回靠近的前k个标签
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 #各个标签出现频率
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) #排序频率
    #python3中：classCount.iteritems()修改为classCount.items()
    #sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list。
    #reverse默认升序 key关键字排序itemgetter（1）按照第一维度排序(0,1,2,3)
    return sortedClassCount[0][0]  #找出频率最高的

```

 