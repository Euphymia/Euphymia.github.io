#最长公共子括号序列 

------

> - 问题
> - 代码
> - 思路

## 问题

最长公共子括号序列

一个合法的括号匹配序列被定义为:

\1. 空串""是合法的括号序列

\2. 如果"X"和"Y"是合法的序列, 那么"XY"也是一个合法的括号序列

\3. 如果"X"是一个合法的序列, 那么"(X)"也是一个合法的括号序列

\4. 每个合法的括号序列都可以由上面的规则生成

例如"", "()", "()()()", "(()())", "(((()))"都是合法的。

从一个字符串S中移除零个或者多个字符得到的序列称为S的子序列。

例如"abcde"的子序列有"abe", "", "abcde"等。

定义LCS(S, T)为字符串S和字符串T最长公共子序列的长度, 即一个最长的序列W既是S的子序列也是T的子序列的长度。

小易给出一个合法的括号匹配序列s, 小易希望你能找出具有以下特征的括号序列t:

1、t跟s不同, 但是长度相同

2、t也是一个合法的括号匹配序列

3、LCS(s, t)是满足上述两个条件的t中最大的

因为这样的t可能存在多个, 小易需要你计算出满足条件的t有多少个。

 

如样例所示: s = "(())()", 跟字符串s长度相同的合法括号匹配序列有:

"()(())", "((()))", "()()()", "(()())", 其中LCS("(())()", "()(())")为4, 其他三个都为5, 所以输出3. 

输入描述:

输入包括字符串s(4 ≤ | s | ≤ 50, | s | 表示字符串长度), 保证s是一个合法的括号匹配序列。

 

 

输出描述:

输出一个正整数, 满足条件的t的个数。

 

输入例子1:

(())()

 

输出例子1:

3

## 代码

```python
strin=input()
strlist=[i for i in strin]
res=[]
# print(strlist)
i=0
def istrue(str1):
    stack=[]
    i=0
    while i<len(str1):
        if len(stack)==0:
            stack.append(str1[i])
            i+=1
            continue
        if str1[i]=='(':
            stack.append(str1[i])
            i+=1
        else:
            if len(stack)>0 and stack.pop(-1)=='(':
                i+=1
                continue
            else:
                return False
    if len(stack)>0:
        return False
    else:
        return True
while i<len(strin):
    if i<len(strin)-1 and strlist[i]==strlist[i+1]:
        i+=1
        continue
    temp=strlist[i]
    del(strlist[i])
    strtemp=strlist
    j=0
    while j<len(strtemp):
        strtemp.insert(j, temp)
        if istrue(strtemp):
            res.append(''.join(strtemp))
        del(strtemp[j])
        j+=1
    strlist.insert(i,temp)
    i+=1

print(len(set(res))-1)
```

## 思路

思路

这里的思路很简单

先创建一个判断是否是合法括号序列的函数

然后开始处理输入的括号序列，依次删除输入序列各个位置的括号(跳过连续重复的括号)，再将删除的括号依次插入剩下的序列的缝隙中，如果仍是合法括号序列，则将其加入res中，继续循环。

输出len(set(res))-1，减一是减去输入序列本身。

因为肯定存在只移动一个括号就合法的新括号序列(此时长度最长)，所以只考虑移动一个括号即可