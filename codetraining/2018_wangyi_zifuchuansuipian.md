#2018_网易_字符串碎片 

------

> - 问题
> - 代码
> - 方法

---

## 问题 

字符串碎片

一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。例如, "aaabbaaac"是由下面碎片组成的: 'aaa', 'bb', 'c'。牛牛现在给定一个字符串, 请你帮助计算这个字符串的所有碎片的平均长度是多少。

输入描述:

输入包括一个字符串s, 字符串s的长度length(1 ≤ length ≤ 50), s只含小写字母('a'-'z')

输出描述:

输出一个整数, 表示所有碎片的平均长度, 四舍五入保留两位小数。

如样例所示: s = "aaabbaaac"

所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25

输入例子1:

aaabbaaac

输出例子1:

2.25

## 代码

```python
str1=input()

i=0
length_sum=0
count=0
while i<len(str1):
    length_add=1
    while i<len(str1)-1 and str1[i]==str1[i+1]:
        length_add+=1
        i+=1
    length_sum+=length_add
    count+=1
    i+=1

print('%0.2f'%(length_sum/count))

```

## 方法

```python
输出保留两位小数
print('%0.2f' % (length_sum/count))
```

