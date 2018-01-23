# 使用SVM处理多分类问题

---

> * 将标签中的字符转换成int类型表示
> * 使用sklearn的svm函数处理多分类问题
> * 代码实现

---

## 代码实现

```python
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score
from sklearn import model_selection
import numpy as np
#由于svm只能处理数值数据，所以先将iris中的字符型标签转换成int类型
def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]
#加载数据时进行转换
data=np.loadtxt('iris.txt',dtype=float,delimiter=',',converters={4:iris_type})
#划分数据，前四列为x，后面的为y
x, y = np.split(data, (4,), axis=1)
#使用model_selection.train_test_split函数划分训练集和测试集
#random_state=1表示随机选取
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, random_state=1, train_size=0.6)
#初始化SVM，C:误差乘法参数，kernel：选择svm的核函数，包括rbf高斯核，linear线性核，poly多项式核等等
#gamma：Kernel coefficient for 'rbf', 'poly' and 'sigmoid'. If gamma is 'auto' then 1/n_features #will be used instead.
#decision_function_shape:包括ovo，ovr，多分类的策略，一对一，一对多分类
clf = SVC(C=0.8, kernel='rbf', gamma=3, decision_function_shape='ovr')
#开始训练svm
clf.fit(x_train, y_train.ravel())
#测试svm分类结果
print ('训练集测试正确率',clf.score(x_train, y_train) ) # 精度)
print('测试集正确率',clf.score(x_test,y_test))

```

