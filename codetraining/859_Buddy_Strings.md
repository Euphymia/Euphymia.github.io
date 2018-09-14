# 859_Buddy_Strings

---

> * 问题
> * 代码
> * 思路

---

## 问题

859.好友字符串

给定两个字符串A和B 小写字母，true当且仅当我们可以交换两个字母A以便结果相等时返回B。

例1：

输入： A = “ab”，B = “ba”

输出：true

例2：

输入： A = “ab”，B = “ab”

输出：错误

例3：

输入： A = “aa”，B = “aa”

输出：true

例4：

输入： A = “aaaaaaabc”，B = “aaaaaaacb”

输出：true

示例5：

输入： A = “”，B = “aa”

输出：错误

注意：

0 <= A.length <= 20000

0 <= B.length <= 20000

A和B仅包含小写字母。

## 代码

```python
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A==B:
            temp=list(A)
            setA=set(temp)
            if len(setA)==len(temp):
                return False
            else:
                return True
        count = 0
        a=[]
        b=[]
        for i,j in zip(A,B):
            if i==j:
                continue
            else:
                if count<=1:
                    a.append(i)
                    b.append(j)
                    count+=1
                    continue
                else:
                    return False
        if a[0]==b[1] and a[1]==b[0]:
            return True
        else:
            return False

if __name__=="__main__":
    sl=Solution()
    result=sl.buddyStrings("aaababc","aaaaacb")
    print(result)
```

## 思路

思路：

如果两个字符串相等，则将判断其中一个字符串中，是否包含相同的元素，这里使用转换为set再判断长度的方法。

如果不相等，则遍历两个字符串，找出两个不同的字符，保存起来，如果找到多于两个的字符，返回False，再判断保存的两个字符交换一下是否相等。

如果找不到两个不同的字符，则后面交换判断的时候也不能满足条件，返回False