# 使用神经网络处理多分类问题（keras）

---

> * teras建立神经网络的一般方法
> * 多分类代码（可直接运行）

---

## 利用keras建立神经网络

```
建立一个简单BP神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense, Activation
model = Sequential()  #层次模型
model.add(Dense(12,input_dim=4,init='uniform')) #输入层，Dense表示BP层
model.add(Activation('relu'))  #添加激活函数
model.add(Dense(1,input_dim=12))  #输出层
model.compile(loss='mean_squared_error', optimizer='adma') #编译模型
model.fit(x_train, y_train, nb_epoch = 1000, batch_size = 6) #训练模型1000次
model.save_weights(modelfile) #保存模型权重
下面代码用的就是一般的iris.csv数据
```

## 代码

```python
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder

# load dataset
dataframe = pd.read_csv("iris.csv", header=None)
dataset = dataframe.values
# print(dataset[:,0:4])
X = dataset[1:, 0:4].astype(float)
Y = dataset[1:, 4]

# encode class values as integers
encoder = LabelEncoder()
encoded_Y = encoder.fit_transform(Y)
# convert integers to dummy variables (one hot encoding)
dummy_y = np_utils.to_categorical(encoded_Y)

# define model structure
def baseline_model():
    # model = keras.models.Sequential() 初始化一个神经网络 
    model = Sequential()
    # add 添加一层神经网
    model.add(Dense(output_dim=10, input_dim=4, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=3, input_dim=10, activation='softmax'))
    # Compile model
    # compile(optimizer, loss, class_mode=”categorical”): 
    # 参数： 
    # optimizer: str (优化函数的名称) 或者优化对象.参考 optimizers. 
    # loss: str (目标函数的名称) 或者目标函数. 参考 objectives. 
    # class_mode: 值为”categorical”, “binary”. 用于计算分类正确率或调用 predict_classes方法. 
    # 指标列表metrics：对分类问题，我们一般将该列表设置为metrics=[‘accuracy’]。
    # 指标可以是一个预定义指标的名字,也可以是一个用户定制的函数.指标函数应该返回单个张量,
    # 或一个完成metric_name - > metric_value映射的字典.
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
# splitting data into training set and test set. If random_state is set to an integer, the split datasets are fixed.
X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.3, random_state=0)
#KerasClassifier创建一个Keras分类器
#build_fn：分类所用的方法
estimator = KerasClassifier(build_fn=baseline_model)
#输入训练集
# #nb_epoch：迭代的次数
# batch_size：每次迭代的样本数目
estimator.fit(X_train, Y_train,nb_epoch=4000, batch_size=256)
# make predictions
pred = estimator.predict(X_test)
# inverse numeric variables to initial categorical labels
#encoder.inverse_transform将按照前面编码的规则反回编码的初始值，比如0-->Iris-setosa
init_lables = encoder.inverse_transform(pred)
# # k-fold cross-validate
# seed = 42
# np.random.seed(seed)
# kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
# results = cross_val_score(estimator, X, dummy_y, cv=kfold)
```

