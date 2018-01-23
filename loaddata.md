# How to load data set？

---

> * python 加载数据集(一)
> * python 加载数据集(二)
> * 使用pandas加载数据(推荐)

---

## python加载数据集(一)

思路，先读取文件(txt，csv)，然后将以','将每行数据(每个样本)分割，获取feature的值，然后根据一行数据的长度，用for循环，将所有的数据全部变为float类型。

```python
#载入数据
def loadDataSet():
    dataMat = []; labelMat = []
#data.txt为当前目录下存在的一个数据集
    fr = open("data.txt",'r')
    for line in fr.readlines():
#strip()出除每行的'\n'，split函数将数据按','划分
        lineArr = line.strip().split(',')
        for i in range(len(lineArr)):
             lineArr[i]=float(lineArr[i])
#将数据除最后一列全部保存到dataMat[]中
        dataMat.append(lineArr[0:-1])
#最后一列是label值，取出保存到labelMat[]中
        labelMat.append(lineArr[-1])
        # i+=1
    return dataMat,labelMat
```

## python加载数据集(二)

思路，与上一种方法很相似，不过这种在数据类型转换时使用了astype(float)方法，更为简洁

```python
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open("Tic-Tac-toe/Tic-Tac-toe.txt",'r')
    for line in fr.readlines():  
        lineArr = line.strip().split(',')
        #将列表lineArr转换成numpy类型
        lineArr=array(lineArr)
        #使用astype()将数据类型转换成float
        lineArr=lineArr.astype(float)

        dataMat.append(lineArr[:-1])
        labelMat.append(lineArr[-1])
        # i+=1
    return dataMat,labelMat
```



## pandas加载数据

要求加载的数据以float的形式保存在矩阵中。pandas为我们提供了很方便的函数。这里使用了很常见的iris的数据。

```python
# load dataset
# 读取csv文件(数据以','分隔)，并保存到pandas的dataframe数据结构中
dataframe = pd.read_csv("iris.csv", header=None)
# 查看dataframe中的内容，发现pandas已自动为每行和列表号(从0开始)
print(dataframe.head())
#              0           1            2           3            4
# 0  SepalLength  SepalWidth  PetalLength  PetalWidth         Name
# 1          5.1         3.5          1.4         0.2  Iris-setosa
# 2          4.9         3.0          1.4         0.2  Iris-setosa
# 3          4.7         3.2          1.3         0.2  Iris-setosa
# 4          4.6         3.1          1.5         0.2  Iris-setosa
# 出去自动加载的标号
dataset = dataframe.values
print(dataset)
# [['SepalLength' 'SepalWidth' 'PetalLength' 'PetalWidth' 'Name']
#  ['5.1' '3.5' '1.4' '0.2' 'Iris-setosa']
#  ['4.9' '3.0' '1.4' '0.2' 'Iris-setosa']
#  ['4.7' '3.2' '1.3' '0.2' 'Iris-setosa']
#  ['4.6' '3.1' '1.5' '0.2' 'Iris-setosa']
#  ['5.0' '3.6' '1.4' '0.2' 'Iris-setosa']
#  ['5.4' '3.9' '1.7' '0.4' 'Iris-setosa']
# 获取前四列的所有数据并转换成float类型
# astype(float)用于类型转换
X = dataset[1:, 0:4].astype(float)
print(X)
# [[ 5.1  3.5  1.4  0.2]
#  [ 4.9  3.   1.4  0.2]
#  [ 4.7  3.2  1.3  0.2]
#  [ 4.6  3.1  1.5  0.2]
#  [ 5.   3.6  1.4  0.2]
#  [ 5.4  3.9  1.7  0.4]
#  [ 4.6  3.4  1.4  0.3]
#  [ 5.   3.4  1.5  0.2]
Y = dataset[1:, 4]
```

