# python高级编程

---

> * import导入模块，避免循环导入
> * ==，is的区别
> * 浅拷贝，深拷贝
> * 私有化
> * 属性property    
> * 使⽤type创建类    
> * 元类__metaclass__属性    
> * 装饰器，闭包函数
> * 垃圾回收，(引用计数，隔代回收)
> * 垃圾回收机制,引用计数，及其漏洞循环引用
> * map函数    

---

### import导入模块，避免循环导入

```python
#import xxx时，程序将会在当前路径及系统path路径中找寻想要导入的模块。如下，一旦找到，停止寻找。
>>> import sys
>>> sys.path
['',
'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36', 'C:\\Users\\Euphy\\AppData\\Roaming\\Python\\Python36\\site-packages', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\qlearning4k-0.0.1-py3.6.egg']
#可以通过append方法，暂时增加系统路径，如：
>>> sys.path.append('C:')
>>> sys.path
['', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36', 'C:\\Users\\Euphy\\AppData\\Roaming\\Python\\Python36\\site-packages', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 'C:\\Users\\Euphy\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\qlearning4k-0.0.1-py3.6.egg', 'C:']
#怎样避免循环导⼊
#1. 程序设计上分层， 降低耦合
#2. 导⼊语句放在后⾯需要导⼊时再导⼊， 例如放在函数体内导⼊
```

### ==，is的区别

1、is 比较两个对象的 id 值是否相等，是否指向同一个内存地址； 

2、== 比较的是两个对象的内容是否相等，值是否相等； 

3、小整数对象[-5,256]在全局解释器范围内被放入缓存供重复使用；

4、is 运算符比 == 效率高，在变量和None进行比较时，应该使用 is。 

- is 比较的是**两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同**。莱布尼茨说过：“世界上没有两片完全相同的叶子”，这个is正是这样的比较，比较是不是同一片叶子（即比较的id是否相同，这id类似于人的身份证标识）。
- == 比较的是**两个对象的内容是否相等，即内存地址可以不一样，内容一样就可以了**。这里比较的并非是同一片叶子，可能叶子的种类或者脉络相同就可以了。默认会调用对象的 **__eq__()**方法。

### 浅拷贝，深拷贝

1，深浅拷贝都是对源对象的复制，占用不同的内存空间。如果拷贝的对象内部还有引用，则一次递归调用deepcopy继续将引用的对象拷贝下来

深拷贝需要

import copy

使用copy.deepcopy()方法	

2，不可变类型的对象，对于深浅拷贝毫无影响，最终的地址值和值都是相等的。

3，可变类型： 
=浅拷贝： 值相等，地址相等 
copy浅拷贝：值相等，地址不相等 ，只拷贝第一层
deepcopy深拷贝：值相等，地址不相等，递归拷贝所有内容
###私有化
​	xx: 公有变量
	_x: 单前置下划线,私有化属性或⽅法， from somemodule import *禁⽌导⼊,类对象和⼦类可以访问
	__xx： 双前置下划线,避免与⼦类中的属性命名冲突， ⽆法在外部直接访问(名字重整所以访问不到)
__	xx__:双前后下划线,⽤户名字空间的魔法对象或属性。 例如: __init__ , __ 不要⾃⼰发明这样的名字
	xx_:单后置下划线,⽤于避免与Python关键词的冲突
	通过name mangling（名字重整(⽬的就是以防⼦类意外重写基类的⽅法或者
属性)如： _Class__object） 机制就可以访问private了

总结 

​	⽗类中属性名中带__  的， ⼦类不继承， ⼦类不能访问 __

​	如果在⼦类中向 __名字 赋值， 那么会在⼦类中定义的⼀个与⽗类相同 名字的属性

​	_名 的变量、 函数、 类在使⽤ from xxx import * 时都不会被导⼊    

###属性property

```python
#1. 私有属性添加getter和setter⽅法
class Money(object):
	def __init__(self):
		self.__money = 0
	def getMoney(self):
		return self.__money
	def setMoney(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")
#2. 使⽤property升级getter和setter⽅法
class Money(object):
	def __init__(self):
		self.__money = 0
	def getMoney(self):
		return self.__money
	def setMoney(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")
	money = property(getMoney, setMoney)
#运⾏结果:
In [1]: from get_set import Money
In [2]:
In [2]: a = Money()
In [3]:
In [3]: a.money
Out[3]: 0
In [4]: a.money = 100
In [5]: a.money
Out[5]: 100
In [6]: a.getMoney()
Out[6]: 100
#3. 使⽤property取代getter和setter⽅法
#@property 成为属性函数， 可以对属性赋值时做必要的检查， 并保证代码的清晰短⼩， 主要有2个作
#⽤将⽅法转换为只读重新实现⼀个属性的设置和读取⽅法,可做边界判定
class Money(object):
	def __init__(self):
		self.__money = 0
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")
#运⾏结果
In [3]: a = Money()
In [4]:
In [4]:
In [4]: a.money
Out[4]: 0
In [5]: a.money = 100
In [6]: a.money
Out[6]: 100
```

### 使⽤type创建类    

​	type除了查看类型外，还有⼀种完全不同的功能， 动态的创建类。 type可以接受⼀个类的描述作为参数， 然后返回⼀个类。 （要知道， 根据传 ⼊参数的不同， 同⼀个函数拥有两种完全不同的⽤法是⼀件很傻的事情， 但 这在Python中是为了保持向后兼容性）    

```python
#type(classname,(parents,...),{attribute})
#第一个参数classname是类名,第二个是一个父类元组，没有可填空元组，第三个参数是类属性字典。
#type可以像这样⼯作：
#type(类名, 由⽗类名称组成的元组（针对继承的情况， 可以为空） ， 包含属性的字典（名称和值） #)⽐如下⾯的代码：
In [2]: class Test: #定义了⼀个Test类
...: pass
...:
In [3]: Test() #创建了⼀个Test类的实例对象
Out[3]: <__main__.Test at 0x10d3f8438>
#可以⼿动像这样创建：
Test2 = type("Test2",(),{}) #定了⼀个Test2类
In [5]: Test2() #创建了⼀个Test2类的实例对象
Out[5]: <__main__.Test2 at 0x10d406b38>
```

### 元类__metaclass__属性   

```python
class Foo(metaclass=something):   #py3
    __metaclass__ = something…
当我们写如下代码时 :

class Foo(Bar):
    pass
在该类并定义的时候，它还没有在内存中生成，知道它被调用。Python做了如下的操作：
1）Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
2）如果Python没有找到__metaclass__，它会继续在父类中寻找__metaclass__属性，并尝试做和前面同样的操作。
3）如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
4）如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

现在的问题就是，你可以在__metaclass__中放置些什么代码呢？
答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东西都可以。
```

### 装饰器，闭包函数

```python
# 闭包函数
def func(funcName):
    def func_inner(*args,**argsw):
        return funcName(*args,**argsw)

    return func_inner

def addfunc(a,b):
    print(a,b)
    return a+b

res=func(addfunc)
print(res(1,2))

# 装饰器
@func
def timefunc(a,b):
    print(a,b)
    return a*b

print(timefunc(2,3))
```

### 垃圾回收

1. ⼩整数对象池 整数在程序中的使⽤⾮常⼴泛， Python为了优化速度， 使⽤了⼩整数对象 池， 避免为整数频繁申请和销毁内存空间。 Python 对⼩整数的定义是 [-5, 257) 这些整数对象是提前建⽴好的， 不会被 垃圾回收。 在⼀个 Python 的程序中， 所有位于这个范围内的整数使⽤的都 是同⼀个对象. 同理， 单个字⺟也是这样的。 但是当定义2个相同的字符串时， 引⽤计数为0， 触发垃圾回收 
2. ⼤整数对象池 每⼀个⼤整数， 均创建⼀个新的对象。    
3. intern机制    a1 = "HelloWorld" a2 = "HelloWorld" a3 = "HelloWorld" a4 = "HelloWorld" a5 = "HelloWorld" a6 = "HelloWorld" a7 = "HelloWorld" a8 = "HelloWorld" a9 = "HelloWorld" python会不会创建9个对象呢？ 在内存中会不会开辟9个”HelloWorld”的内存 空间呢？ 想⼀下， 如果是这样的话， 我们写10000个对象， ⽐如 a1=”HelloWorld”…..a1000=”HelloWorld”， 那他岂不是开辟了1000 个”HelloWorld”所占的内存空间了呢？ 如果真这样， 内存不就爆了吗？ 所以 python中有这样⼀个机制—— intern机制 ， 让他只占⽤⼀个”HelloWorld”所 占的内存空间。 靠引⽤计数去维护何时释放。   
4. 总结 ⼩整数[-5,257)共⽤对象， 常驻内存 单个字符共⽤对象， 常驻内存 单个单词， 不可修改， 默认开启intern机制， 共⽤对象， 引⽤计数为0， 则销毁    
5. 字符串（含有空格） ， 不可修改， 没开启intern机制， 不共⽤对象， 引⽤ 计数为0， 销毁    
6. ⼤整数不共⽤内存， 引⽤计数为0， 销毁    
7. 数值类型和字符串类型在 Python 中都是不可变的， 这意味着你⽆法修改 这个对象的值， 每次对变量的修改， 实际上是创建⼀个新的对象    

###垃圾回收机制,引用计数，及其漏洞循环

```python
# python引用计数垃圾回收机制的漏洞，循环引用。
class A:
    def __init__(self):
        print('object born , id :%s'%str(hex(id(self))))
def fun1():
    while True:
        c1=A()
        c2=A()
        c1.t=c2
        c2.t=c1
        del c1
        del c2

fun1()
```

### map函数    

map函数会根据提供的函数对指定序列做映射 map(...) map(function, sequence[, sequence, ...]) -> list function:是⼀个函数 sequence:是⼀个或多个序列,取决于function需要⼏个参数 返回值是⼀个list 参数序列中的每⼀个元素分别调⽤function函数， 返回包含每次function函数 返回值的list。    

```python
#函数需要⼀个参数
map(lambda x: x*x, [1, 2, 3])
#结果为:[1, 4, 9]
#函数需要两个参数
map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
#结果为:[5, 7, 9]
def f1( x, y ):
return (x,y)
l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
l3 = map( f1, l1, l2 )
print(list(l3))
#结果为:[(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5, 
```



