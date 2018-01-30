# Sklearn 的一些方法

---

> * Sklearn-train_test_split随机划分训练集和测试集
> * 标签二值化LabelBinarizer

---

## Sklearn-train_test_split随机划分训练集和测试集

参数解释：

train_data：所要划分的样本特征集

train_target：所要划分的样本结果

test_size：样本占比，如果是整数的话就是样本的数量

random_state：是随机数的种子。

随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。

随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：

种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。

## 标签二值化LabelBinarizer

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

