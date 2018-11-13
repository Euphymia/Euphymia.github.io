#937_Reorder_Log_Files

------

> - 问题
> - 代码
> - 思路

------

## 问题

 \937. 重新排列日志文件

你有一个日志数组 logs。每条日志都是以空格分隔的字串。

 

对于每条日志，其第一个字为字母数字标识符。然后，要么：

 

标识符后面的每个字将仅由小写字母组成，或；

标识符后面的每个字将仅由数字组成。

我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

 

将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按字母顺序排序，忽略标识符，标识符仅用于表示关系。数字日志应该按原来的顺序排列。

 

返回日志的最终顺序。

 

示例 ：

 

输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

 

提示：

 

0 <= logs.length <= 100

3 <= logs[i].length <= 100

logs[i] 保证有一个标识符，并且标识符后面有一个字。

 

## 代码

```python
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        str_list = [x for x in logs if not str.isdigit(x.split()[1])]
        num_list = [x for x in logs if str.isdigit(x.split()[1])]
        order_str = sorted(str_list, key=lambda x: " ".join(x.split()[1:]))
        return order_str + num_list

if __name__=='__main__':
    sl=Solution()
    logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(sl.reorderLogFiles(logs))
```

## 思路

​    思路很简单，首先将logs里的字母日志和数字日志分开然后，对字母日志按第二个元素进行排序，最后拼接到一起。

### sorted的使用方法

```python
方法：sorted
    高级用法
有时候，我们要处理的数据内的元素不是一维的，而是二维的甚至是多维的，那要怎么进行排序呢？这时候，sorted()函数内的key参数就派上用场了！
从帮助信息上可以了解到，key参数可传入一个自定义函数。那么，该如何使用呢？让我们看看如下代码：
>>>l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
>>>sorted(l, key=lambda x:x[0])
Out[39]: [('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
>>>sorted(l, key=lambda x:x[0], reverse=True)
Out[40]: [('e', 3), ('d', 4), ('c', 6), ('b', 2), ('a', 1)]
>>>sorted(l, key=lambda x:x[1])
Out[41]: [('a', 1), ('b', 2), ('e', 3), ('d', 4), ('c', 6)]
>>>sorted(l, key=lambda x:x[1], reverse=True)
Out[42]: [('c', 6), ('d', 4), ('e', 3), ('b', 2), ('a', 1)]
这里，列表里面的每一个元素都为二维元组，key参数传入了一个lambda函数表达式，其x就代表列表里的每一个元素，
然后分别利用索引返回元素内的第一个和第二个元素，这就代表了sorted()函数利用哪一个元素进行排列。而reverse参数就如同上面讲的一样，
起到逆排的作用。默认情况下，reverse参数为False。
当然，正如一开始讲到的那样，如果想要对列表直接进行排序操作，可以用成员方法sort()来做：

>>>l.sort(key=lambda x : x[1])
>>>l
Out[45]: [('a', 1), ('b', 2), ('e', 3), ('d', 4), ('c', 6)]
>>>l.sort(key=lambda x : x[1], reverse=True)
>>>l
Out[47]: [('c', 6), ('d', 4), ('e', 3), ('b', 2), ('a', 1)]
```

 