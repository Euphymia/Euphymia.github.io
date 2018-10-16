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
> * map()的使用方法
> * python 中的三元表达式（三目运算符）
> * python 中lambda()的用法
> * Python高级数据结构-Collections模块
> * 字符串倒序
> * 输出保留两位小数
> *  remove，del，pop的区别 

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

### map()的使用方法

```python
描述
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法
map() 函数语法：

map(function, iterable, ...)
参数
function -- 函数，有两个参数
iterable -- 一个或多个序列
返回值
Python 2.x 返回列表。

Python 3.x 返回迭代器。

实例
以下实例展示了 map() 的使用方法：

>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
```

### python 中的三元表达式（三目运算符）

```python
a = 1
b = 2
h = ""
h = a-b if a>b else a+b
print(h)
```

###python 中lambda()的用法

```python
在python中有一个匿名函数lambda，匿名函数顾名思义就是指：是指一类无需定义标识符（函数名）的函数或子程序。在C++11和C#中都有匿名函数的存在。下面看看在python中匿名函数的使用。

1.lambda只是一个表达式，函数体比def简单很多。

2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

3.lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。

例1.定义一个lambda表达式，求三个数的和

# -*- coding: UTF-8 -*-
f = lambda x,y,z:x + y + z

print f(1,2,3)
print f(4,5,6)

输出：
6
15
```

### Python高级数据结构-Collections模块

这个模块对上面的数据结构做了封装，增加了一些很酷的数据结构，比如：

a）Counter： 计数器，用于统计元素的数量

b）OrderDict：有序字典

c）defaultdict：值带有默认类型的字典

d）namedtuple：可命名元组，通过名字来访问元组元素

e）deque :双向队列，队列头尾都可以放，也都可以取（与单向队列对比，单向队列只能一头放，另一头取）#

```python
#1. Counter
#通过字典形式统计每个元素重复的次数传  
res = collections.Counter('abcdabcaba')  
print(res)                                  #结果Counter({'a': 4, 'b': 3, 'c': 2, 'd': 1})  
  
#dict的子类，所以也可以以字典的形式取得键值对  
for k in res:  
    print(k, res[k], end='  |  ')           #结果 a 4  |  b 3  |  c 2  |  d 1  |  
for k, v in res.items():  
    print(k, v, end='  |  ')                #结果 a 4  |  b 3  |  c 2  |  d 1  |  
  
#通过most_common(n)，返回前n个重复次数最多的键值对  
print(res.most_common())                    #结果None  
print(res.most_common(2))                   #结果[('a', 4), ('b', 3)]  
  
#通过update来增加元素的重复次数，通过subtract来减少元素重复的次数  
a = collections.Counter('abcde')  
res.update(a)  
print(res)                                  #结果Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})，比原来的res增加了重复次数  
  
b = collections.Counter('aaafff')  
res.subtract(b)  
print(res)                                  #结果Counter({'b': 4, 'c': 3, 'a': 2, 'd': 2, 'e': 1, 'f': -3})，还有负值，要注意  
  
#fromkeys功能还没实现，使用的话会报错
2. OrderDict

#有序字典，数据结构字典Dict是无序的，有时使用起来不是很方便，Collections里提供一个有序字典OrderDict，用起来就很方便了
#在介绍有序字典以前，用已知的知识其实可以自己实现一个有序字典，通过列表或者元祖来维护key，实现有序字典：
lst =[]
dic = {}

lst.append('name')
dic['name'] = 'winter'
lst.append('age')
dic['age'] = 18

for k in lst:
    print(k, dic[k])
#实例：

#dict的方法OrderDict基本都可以使用，比如keys(), values(), clear()

#注意，因为OrderDict有序，有些方法不同，比如，pop()和popitem()

#另外OrderDict增加了一个move_to_end的方法
#创建一个有序字典
dic = collections.OrderedDict()
dic['name'] = 'winter'
dic['age'] = 18
dic['gender'] = 'male'

print(dic)                         #结果OrderedDict([('name', 'winter'), ('age', 18), ('gender', 'male')])

#将一个键值对放入最后
dic.move_to_end('name')
print(dic)                         #结果OrderedDict([('age', 18), ('gender', 'male'), ('name', 'winter')])

#3. defaultdict

#默认字典，为字典设置一个默认类型；很有用，比如说：
people = [['male', 'winter'], ['female', 'elly'], ['male', 'frank'], ['female', 'emma']]
#将男性女性分开，所有男性放到'male'中，所有女性放放到'female'中
gender_sort = {}

for info in people:
    if info[0] in gender_sort:
        gender_sort[info[0]].append(info[1])
    else:
        gender_sort[info[0]] = [info[1]]

print(gender_sort)                              #结果{'male': ['winter', 'frank'], 'female': ['elly', 'emma']}
#如果使用defaultdict就会简单很多
people = [['male', 'winter'], ['female', 'elly'], ['male', 'frank'], ['female', 'emma']]

gender_sort = collections.defaultdict(list)
for info in people:
    gender_sort[info[0]].append(info[1])

print(gender_sort)      #结果defaultdict(<class 'list'>, {'male': ['winter', 'frank'], 'female': ['elly', 'emma']})

#4. namedtuple
#可命名元组，给元组每个元素起一个名字，这样就可以通过名字来访问元组里的元素，增强了可读性；尤其对于坐标，html标签的长宽等，使用名字可读性更强；有点类似于字典了
position_module = collections.namedtuple('position', ['x', 'y', 'z'])   #'position'相当于指定一个类型，类似于上面的OrderedDict([('age', 18), ('gender', 'male'), ('name', 'winter')])中的OrderdDict

a_position = position_module(3, 5, 7)
print(a_position)                                   #结果position(x=3, y=5, z=7)
print(a_position.x, a_position.y, a_position.z)     #结果3 5 7
import collections

login_user = [
    (r'http://www.baidu.com', 'usr1', 'pwd1'),
    (r'http://www.youdao.com', 'usr2', 'pwd2'),
    (r'http://mail.126.com', 'usr3', 'pwd3')
]

page_info = collections.namedtuple('login_info', ['url', 'username', 'password'])
for user in login_user:
    x = page_info(*user)
    print(x)
#结果：
login_info(url='http://www.baidu.com', username='usr1', password='pwd1')
login_info(url='http://www.youdao.com', username='usr2', password='pwd2')
login_info(url='http://mail.126.com', username='usr3', password='pwd3')

#5. deque

#deque其实是 double-ended queue 的缩写，双向队列

 #说到队列就要说到队列和栈了；队列是FIFO，栈是FILO

#队列又分为：单向队列（只能从一边放，从另外一边取）；双向队列（两头都可以放，也都可以取）

#Python中单向队列就是queue.Queue
raw = [1,2,3]
d = collections.deque(raw)
print(d)                    #结果deque([1, 2, 3])

#右增
d.append(4)
print(d)                    #结果deque([1, 2, 3, 4])
#左增
d.appendleft(0)
print(d)                    #结果deque([0, 1, 2, 3, 4])

#右扩展
d.extend([5,6,7])
print(d)                    #结果deque([0, 1, 2, 3, 4, 5, 6, 7])
#左扩展
d.extendleft([-3,-2,-1])
print(d)                    #结果deque([-1, -2, -3, 0, 1, 2, 3, 4, 5, 6, 7])

#右弹出
r_pop = d.pop()
print(r_pop)                #结果7
print(d)                    #结果deque([-1, -2, -3, 0, 1, 2, 3, 4, 5, 6])
#左弹出
l_pop = d.popleft()
print(l_pop)                #结果-1
print(d)                    #结果deque([-2, -3, 0, 1, 2, 3, 4, 5, 6])

#将右边n个元素值取出加入到左边
print(d)                    #原队列deque([-2, -3, 0, 1, 2, 3, 4, 5, 6])
d.rotate(3)
print(d)                    #rotate以后为deque([4, 5, 6, -2, -3, 0, 1, 2, 3])
```

### 字符串倒序

```python
res=res[::-1]
```

### 输出保留两位小数

```python
print('%0.2f' % (length_sum/count))
```

### remove，del，pop的区别 

```python
remove 是删除首个符合条件的元素。并不是删除特定的索引。
>> > a = [0, 2, 2, 3]
>> > a.remove(2)
>> > a
[0, 2, 3]
而对于 del 来说，它是根据索引（元素所在位置）来删除的
>> > a = [3, 2, 2, 1]
>> > del a[1]
[3, 2, 1]
pop返回的是你弹出的那个数值
>> > a = [4, 3, 5]
>> > a.pop(1)
3
>> > a
[4, 5]
字符串与数组相互转换
字符串转数组

str = '1,2,3'
arr = str.split(',')
print a
数组转字符串

#方法1
arr = ['a', 'b']
str1 = ','.join(arr)
print str1
```
