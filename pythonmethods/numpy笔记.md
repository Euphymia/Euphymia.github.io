# Notes of numpy

---

> * np.ones() and np.zeros()
> * np.array()
> * np.arange()
> * np.reshape() and shape
> * np.linspace()
> * np.newaxis()
> * np.random()
> * np.expand_dims()

---

##  np.ones() and np.zeros()

np.ones() ,np.zeros()define a unit vector or zero vector

```python
print(np.ones(6))
#>>> [1,1,1,1,1,1]
print(np.ones(6).reshape(2,3))
#>>> [[1,1,1]
#     [1,1,1]]
print(np.ones((2,3)))
#>>> [[1,1,1]
#     [1,1,1]]
print(np.zeros((2,3)))
#>>> [[0,0,0]
#      [0,0,0]]
```

## np.array()

np.array() define a matrix

```python
print(np.array([1,1,1,3,4,5]).reshape(2,3,))
#>>> [[1,1,1]
#     [3,4,5]]
print(np.array([(1,2,3),(4,5,6)]))
# >>> [[1 2 3]
#      [4 5 6]]
```

## np.arange()

np.arange() 生成一个连续的(步长可设)向量，step表示步长

 ```python
print(np.arange(24,step=2).reshape(3,4))
#>>> [[ 0  2  4  6]
#     [ 8 10 12 14]
#     [16 18 20 22]]
 ```

##np.reshape() and shape

reshape()可以对数组重新排列，shape用来获取当前矩阵的行列数据(不要括号，因为是一个属性)

```python
a=np.arange(20).reshape(4,5)
print(a.shape)
#>>> (4, 5)
```

##np.linspace()

np.linspace()生成一个连续的(数量可设)向量，restep=True表示输出一个元组，元组的两个元素分别是需要生成的数列和数列的步进差值

```python
print(np.linspace(1,10,num=10,retstep=True))
#(array([  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.]), 1.0)
print(np.linspace(1,10,num=10,retstep=False))
#>>> [  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
#generate num=10(default=50) number  between(1,10)
```

##np.newaxis()

np.newaxis   插入新维度， 例如在(6,)的数组添加[;,np.newaxis]，将变为(6,1)，添加[np.newaxis,;],变为(1,6)

```python
print(np.linspace(-1,1,3)[:,np.newaxis])
#>>> [[-1.]
#     [ 0.]
#     [ 1.]]
```

## np.random()

1.numpy.random.rand(d0, d1, ..., dn)：生成一个[0,1)之间的随机浮点数或N维浮点数组。

```python
print(np.random.rand(2,3))
#>>> [[ 0.80992922  0.53225615  0.56893405]
#     [ 0.49443502  0.97166826  0.08645615]]
```

2.numpy.random.randn(d0, d1, ..., dn)：生成一个浮点数或N维浮点数组，取数范围：正态分布的随机样本数。

``` python
print(np.random.randn(2,3))
#>>> [[-0.80185247 -1.85945625  1.05123697]
#     [-0.3970562   0.08562274  1.28801424]]
```

3.numpy.random.standard_normal(size=None)：生产一个浮点数或N维浮点数组，取数范围：标准正态分布随机样本，与randn很像，只是输入时不同，这里输入只有一个，size=(row,column)

```python
#输入只有一个
print(np.random.standard_normal((2,3)))
#>>> [[ 0.8726317   0.57602787 -0.48375792]
#     [-0.12407604  0.79319393 -0.50077359]]
```

4.numpy.random.randint(low, high=None, size=None, dtype='l')：生成一个整数或N维整数数组，取数范围：若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数。

```python
没有传入high的值时生成[0,low)之间的随机整数
print(np.random.randint(5,size=(2,3)))
#>>> [[3 4 4]
#     [2 0 1]]
传入high的值时，生成[low,high)之间的随机整数
print(np.random.randint(5,high=10,size=(2,3)))
#>>> [[9 9 7]
#     [8 7 5]]
```

5.numpy.random.random_integers(low, high=None, size=None)：生成一个整数或一个N维整数数组，取值范围：若high不为None，则取[low,high]之间随机整数，否则取[1,low]之间随机整数。

```python
没有传入high的值时生成[0,low]之间的随机整数
print(np.random.random_integers(5,size=(2,3)))
#>>> [[1 5 3]
#     [2 5 2]]
传入high的值时，生成[low,high]之间的随机整数
print(np.random.random_integers(5,high=10,size=(2,3)))
#>>> [[ 5 10  5]
#     [ 8 10  8]]
```

6.numpy.random.random_sample(size=None)：生成一个[0,1)之间随机浮点数或N维浮点数组。与rand很像，只是输入不一样，这里是有一个输入，size=(row,column)

```python
print(np.random.random_sample((2,3)))
#>>> [[ 0.61281073  0.93650569  0.59190112]
#     [ 0.27335348  0.16329731  0.14627115]]
```
7.numpy.random.shuffle(x)

Modify a sequence in-place by shuffling its contents.

| Parameters: | **x** : array_likeThe array or list to be shuffled. |
| ----------- | ---------------------------------------- |
| Returns:    | None                                     |

```python
idx=list(range(10))
#shuffle的返回值固定为None，所以不能直接打印返回值
np.random.shuffle(idx)
print(idx)
#[5, 8, 7, 9, 3, 4, 6, 1, 0, 2]
```

8.numpy.random.permutation(x)

获取一个一定长度的乱序，输入是一个序列的长度，与numpy.random.shuffle(x)不同，shuffle的输入是一个np数组。

```python
np.random.permutation(10)
array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6])
```



## np.expand_dims()

expand_dims(a, axis)就是在axis的那一个轴上把数据加上去，这个数据在axis这个轴的0位置。 

例如原本为一维的2个数据，axis=0，则shape变为(1,2),axis=1则shape变为(2,1) 

再例如 原本为 (2,3),axis=0，则shape变为(1,2,3),axis=1则shape变为(2,1,3)