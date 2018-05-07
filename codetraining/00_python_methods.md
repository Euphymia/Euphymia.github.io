# python methods

---

> * python运算符
> * set的使用方法
> * for循环的使用方法
> * range() 的使用方法
> * list 的使用方法

---

### python运算符

```python
数字运算符

// 运算符

取整除 - 返回商的整数部分

**运算符

幂 - 返回x的y次幂

%运算符

取余

比较运算符

<>比较运算符 

不等于 - 比较两个对象是否不相等

Python位运算符

按位运算符是把数字看作二进制来进行计算的。

&   

按位与运算符：参与运算的两个值, 如果两个相应位都为1, 则该位的结果为1, 否则为0

|   

按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。

^   

按位异或运算符：当两对应的二进位相异时，结果为1

<< 

左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。

>>  

右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

Python成员运算符

in 

如果在指定的序列中找到值返回 True，否则返回 False。

not in

如果在指定的序列中没有找到值返回 True，否则返回 False。
```

###set的使用方法

```python
# set 无序，不重复序列
# 创建
# 第一种
set1 = {"1", "2"}
# {'1', '2'}
print(type(set1))
# 第二种
list1 = ["1", "2", "2", "1"]
set2 = set(list1)
print(set2)
# {'1', '2'}
# <class 'set'>
# 功能
# 添加一个元素
s = set()
s.add(123)
s.add(123)
print(s)
# {123}
# 清除素有内容
s.clear()
print(s)
# set()
# 两个集合的差集
s1 = {32, 12, 34}
s2 = {12, 43, 23}
# s1中存在，s2中不存在
print(s1.difference(s2))
# {32, 34}
# 对称差集
print(s1.symmetric_difference(s2))
# {32, 34, 43, 23}
# difference和symmetric_different会生成新一个结果，而different_update 和 symmetic_different_update会覆盖之前集合

# 移除元素 如果元素不存在，不会报错 remove 如果元素不存在，会报错
s1.discard(32)
print(s1)
# {34, 12}
# 集合pop随机移除某个元素并且获取那个参数,集合pop没有参数
re2 = s2.pop()
print(re2)
# 43
s3 = {11, 22, 33}
s4 = {44, 33, 22}
# 交集
print(s3.intersection(s4))
# {33, 22}

# 判断两个集合有没有交集,有返回true 无返回false
print(s3)
print(s4)
print(s3.isdisjoint(s4))
# False 怎么是false 这不是有交集吗

# 并集
print(s3.union(s4))
# {33, 22, 11, 44}

# update 批量更新
li = [21, 4, 2, 312]
s3.update(li)
print(s3)
# {33, 2, 4, 11, 21, 22, 312}
```

###for循环的使用方法

```python
python的for循环中不能修改循环变量i，有需求可以用while代替
```

###range() 的使用方法

```python
>> > range(1, 4)
[1, 2, 3]
>> > range(4)
[0, 1, 2, 3]
>> > range(1, 4, 2)
[1, 3]
```

###list 的使用方法

```python
Python列表函数 & 方法
Python包含以下函数:
序号	函数
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表
Python包含以下方法:
序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop(obj=list[-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort([func])
对原列表进行排序
```

