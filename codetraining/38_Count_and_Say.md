#38 Count and Say

---

> * 问题
> * 代码
> * for循环的使用方法
> * range() 的使用方法
> * list 的使用方法

---

## 问题

问题：

报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

\1.     1

\2.     11

\3.     21

\4.     1211

\5.     111221

1 被读作  "one 1"  ("一个一"), 即 11。

11 被读作 "two 1s" ("两个一"）, 即 21。

21 被读作 "one 2",  "one 1" （"一个二",  "一个一"), 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:

输入: 1

输出: "1"

示例 2:

输入: 4

输出: "1211"

## 代码

```python
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res="1"
        if n==1:
            return res
        else:
            i=0
            while i<n-1:
                temp=""
                j=0
                while j<len(res):
                    num=res[j]
                    count=1
                    while j<len(res)-1 and res[j]==res[j+1]:
                        count+=1
                        j+=1
                    temp+=str(count)
                    temp+=str(num)
                    j+=1
                res=temp
                i+=1
        return res
sl=Solution()
res=sl.countAndSay(4)
print(res)
```

## for循环的使用方法

```python
python的for循环中不能修改循环变量i，有需求可以用while代替
```

## range() 的使用方法

```python
>> > range(1, 4)
[1, 2, 3]
>> > range(4)
[0, 1, 2, 3]
>> > range(1, 4, 2)
[1, 3]
```

##list 的使用方法

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

