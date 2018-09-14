# list的一些方法

---

> * 创建一个list的二维零数组
> * append和extend的区别

---

### 创建一个list的二维零数组

```python
b =[[0 for x in range(n)] for y in range(m)]  
# 初始化一个m*n的二维零数组
```

### append和extend的区别

```python
# append()接受一个对象参数，把对象添加到列表的尾部
a=[1,2,3]
a.append([4,5,6])
a
>>> [1, 2, 3, [4, 5, 6]]
#extend()接受一个列表参数，把参数列表的元素添加到列表的尾部
a=[1,2,3]
a.extend([1,2,4])
a
>>> [1, 2, 3, 1, 2, 4]

```

