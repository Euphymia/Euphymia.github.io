# python methods

---

> * python运算符
> * set的使用方法
> * for循环的使用方法
> * range() 的使用方法
> * list 的使用方法
> * 列表交换两个元素
> * 列表append() 方法覆盖前面元素解决方法
> * format的使用方法
> * time.clock()的使用方法
> * 间接修改字符串中字符的方法

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

###python列表交换两个元素

```python

# python列表交换两个元素：

nums[a], nums[b] = nums[b], nums[a]

```

###python.append() 方法覆盖前面元素解决方法

```python

先进行深拷贝

import copy

copy.deepcopy(a)

再将a append到列表中即可

```

###format的使用方法

```python
python中format函数用于字符串的格式化
通过关键字
1 print('{名字}今天{动作}'.format(名字='陈某某', 动作='拍视频'))  # 通过关键字
2 grade = {'name': '陈某某', 'fenshu': '59'}
3 print('{name}电工考了{fenshu}'.format(**grade))  # 通过关键字，可用字典当关键字传入值时，在字典前加**即可
通过位置
1 print('{1}今天{0}'.format('拍视频', '陈某某'))  # 通过位置
2 print('{0}今天{1}'.format('陈某某', '拍视频'))
填充和对齐 ^ < > 分别表示居中、左对齐、右对齐，后面带宽度
1 print('{:^14}'.format('陈某某'))
2 print('{:>14}'.format('陈某某'))
3 print('{:<14}'.format('陈某某'))
4 print('{:*<14}'.format('陈某某'))
5 print('{:&>14}'.format('陈某某'))  # 填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
精度和类型f精度常和f一起使用
1 print('{:.1f}'.format(4.234324525254))
2 print('{:.4f}'.format(4.1))
进制转化，b o d x 分别表示二、八、十、十六进制
print('{:b}'.format(250))
print('{:o}'.format(250))
print('{:d}'.format(250))
print('{:x}'.format(250))
千分位分隔符，这种情况只针对与数字
print('{:,}'.format(100000000))
print('{:,}'.format(235445.234235))
```

###time.clock()的使用方法

```
Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
```

## 间接修改字符串中字符的方法

```python
方法一：将字符串转换为列表，修改列表的元素后，在重新连接为字符串:

str1 = "string"
str2 = list(str1)    #将字符串转换为列表，列表的每一个元素为一个字符
str2[2] = 'x' 
str2 = ''.join(str2)     #将列表重新连接为字符串
print(str1,str2)
>>>string stxing
方法二：使用str.replace方法替换成我们想要的字符串，replace函数用法：str.replace(old, new, max)，是把字符串str中的所有old字符子串替换为new，max指定从左往右的最大替换次数，max可省略。

str1 = "string"
str2 = str1.replace(str1[2],'x')    #将字符串第三位替换为x
print(str1,str2)
>>>string stxing

方法三：将字符串切片后相加：

str1 = "string"
str2 = str1[0:2]+'x'+str1[3:]   #先切后合
print(str1,str2)
>>>string stxing
```

​	