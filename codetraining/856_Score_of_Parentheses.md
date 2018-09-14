# 856_Score_of_Parentheses

---

> * 问题
> * 代码
> * 思路

---

## 问题

856.括号的分数 

给定一个平衡的括号字符串S，根据以下规则计算字符串的得分：

() 有1分

AB有得分A + B，其中A和B是平衡的括号字符串。

(A)有得分2 * A，其中A是一个平衡的括号字符串。

例1：

输入：“（）”

输出：1

例2：

输入：“（（））”

输出：2

例3：

输入：“（）（）”

输出：2

例4：

输入：“（（）（（）））”

输出：6

注意：

S是一个平衡的括号字符串，只包含(和)。

2 <= S.length <= 50

## 代码

```python
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack=[]
        parentheses=list(S)
        l=len(parentheses)
        i=0
        while i<l:
            if parentheses[i] == '(':
                stack.append(parentheses[i])
            elif parentheses[i] == ')':
                if stack[-1] == '(':
                    m=stack.pop()
                    parentheses[i]='1'
                    i-=1
                else:
                    m=stack.pop()
                    n=stack.pop()
                    parentheses[i]=str(m*2)
                    i-=1
            else:
                if i == l-1:
                    return stack.pop()+int(parentheses[i]) if len(stack)==1 else int(parentheses[i])
                elif len(stack)==0:
                    stack.append(int(parentheses[i]))
                elif stack[-1]=='(':
                    stack.append(int(parentheses[i]))
                else:
                    m=stack.pop()
                    stack.append(m+int(parentheses[i]))
            i+=1
if __name__=="__main__":
    sl=Solution()
    result=sl.scoreOfParentheses("(())()")
    print(result)

```

## 思路

思路：

先将字符串转为列表形式的符号集，便于对下标进行操作。

由于是标准的括号集。

1.符号集遇到'('直接保存进栈里

2.遇到')'开始进行判断，当前栈顶元素是'('，则弹出栈顶元素，并将分数记为1，保存进符号集(并使之下一次遍历立即被遍历到)

如果当前栈顶元素是一个数，则将这个数乘以2，同样保存进符号集。

3.符号集遇到的是一个数，先考虑是否遍历结束，如果符号集遍历到最后一个，则将当前符号与栈中元素(如果存在)相加输出

如果遇到'(',将符号压进栈中。

如果遇到数字，将其相加，压进栈中