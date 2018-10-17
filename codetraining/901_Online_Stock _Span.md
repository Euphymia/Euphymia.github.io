#Online_Stock _Span

------

> - 问题
> - 代码
> - 思路
> - 方法

## 问题

\901. Online Stock Span

 

写一个类StockSpanner，收集某些股票的每日报价，并返回该 股票当前价格的跨度。

 

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续天数（从今天开始到倒退）。

 

例如，如果未来7天的股票价格是[100, 80, 60, 70, 60, 75, 85]，则股票跨度将是[1, 1, 1, 2, 1, 4, 6]。

 

 

例1：

 

输入：[“StockSpanner”，“next”，“next”，“next”，“next”，“next”，“next”，“next”]，[[]，[100]，[80]，[60]，[70]，[60]，[75]，[85]]

输出：[null，1, 1, 1, 2, 1, 4, 6]

说明：

首先，初始化S = StockSpanner（）。然后：

S.next（100）被调用并返回1，

S.next（80）被调用并返回1，

S.next（60）被调用并返回1，

S.next（70）被调用并返回2，

S.next（60）被调用并返回1，

S.next（75）被调用并返回4，

S.next（85）被调用并返回6。

 

注意（例如）S.next（75）返回4，因为最后4个价格

（包括今天的75的价格）小于或等于今天的价格。

 

 

注意：

 

呼唤StockSpanner.next(int price)将有1 <= price <= 10 ^ 5。

 每个测试用例最多会有一次10000调用StockSpanner.next。

所有测试用例最多都会有150000调用StockSpanner.next。

C + +的此问题的总时间限制减少了75％，所有其他语言的时间限制减少了50％

## 代码

```python
import operator
class StockSpanner:
    
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res
if(__name__ == '__main__'):
    A = [int(i) for i in input()[1:-1].split(',')]
    # B = [int(i) for i in input()[1:-1].split(',')]
    obj = StockSpanner()

    for i in A:
        print(obj.next(i))
```

## 思路

思路：

初始化一个栈用于保存比今日价格高的价格及价格跨度，用一个二维数组表示，第一个位置表示价格，第二个位置表示价格跨度。

从栈顶找出比今日价格低的价格跨度并相加，最终结果再保存到栈顶，以备下次使用。很精妙

 ## 方法

python 字典的操作

\####字典的定义 key: value

info = {

​    'stu1001': "TengLan Wu",

​    'Stu1002': "Longze Loula",

​    'stu1103': "XiaoZe Maliya",

}

\#####查询 字典的数据###############

\#####查询所有，但是字典是无序的

print(info)

 

\#如果查询一个只需要查询对方的key

print(info["stu1001"])

 

\#不报错方式查询（安全点）

print(info.get("stu1001"))

 

 

\####### 修改######

 

info["stu1001"] = "武藤兰"

print(info)

 

\#########添加#########

info["stu1004"] = "CangjingKong"

print(info)

 

\########删除######## 两种方法

\#第一种

\#del info["stu1001"]

print(info)

 

\#第二种

info.pop("stu1103")

print(info)

 

\#还有一个随机删除

info.popitem()

 

\#判断字典里面存不存在这个key

 

print('stu1005' in info)  # 有的话返回TRUE

 

\#查询所有的values

print(info.values())

 

\#查询所有的key

print(info.keys())

 

字典的排序

import operator

dic = {'a': 1, 'f': 2, 'c': 3, 'h': 0}

\# 函数原型：sorted(dic,value,reverse)

\# 按字典中的键进行升序排序

print("按键进行升序排序结果为:",

​        sorted(dic.items(), key=operator.itemgetter(0), reverse=False))

\# 按字典中的键进行降序排序

print("按键进行降序排序结果为:",

​        sorted(dic.items(), key=operator.itemgetter(0), reverse=True))

\# 按字典中的值进行升序排序

print("按值进行升序排序结果为:",

​        sorted(dic.items(), key=operator.itemgetter(1), reverse=False))

\# 按字典中的值进行降序排序

print("按值进行降序排序结果为:",

​        sorted(dic.items(), key=operator.itemgetter(1), reverse=True))

 