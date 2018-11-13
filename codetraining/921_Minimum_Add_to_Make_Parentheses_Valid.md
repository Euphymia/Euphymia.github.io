#921_Minimum_Add_to_Make_Parentheses_Valid

------

> - 问题
> - 代码
> - 思路

------

## 问题

 921.使括号有效的最少添加

给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

 

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

 

它是一个空字符串，或者

它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者

它可以被写作(A)，其中 A 是有效字符串。

给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

示例 1：

输入："())"

输出：1

示例 2：

 

输入："((("

输出：3

示例 3：

输入："()"

输出：0

示例 4：

输入："()))(("

输出：4

提示：

 

S.length <= 1000

S 只包含 '(' 和 ')' 字符。

## 代码

```python
class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left=right=0
        for i in S:
            if i == "(":
                left+=1
            elif i == ")" and left==0:
                right+=1
            else :
                left-=1
        
        return right+left

if __name__=="__main__":
    sl=Solution()
    S="()))(("
    print(sl.minAddToMakeValid(S))

```

## 思路

思路：

很巧妙，根据题意，我们只需找出没有对上括号的单括号数量。