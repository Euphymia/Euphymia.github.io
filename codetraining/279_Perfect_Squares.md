# 279_Perfect_Squares

------

> - 问题
> - 代码
> - 思路

---

## 问题

1. 完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12

输出: 3 

解释: 12 = 4 + 4 + 4.

示例 2:

 

输入: n = 13

输出: 2

解释: 13 = 4 + 9.

## 代码

```python
class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt

if __name__=="__main__":
    sl=Solution()
    print(sl.numSquares(13))
```

## 思路

思路

非常好的代码，使用了dfs的思路

首先获取所有小于n的平方项，用于之后的搜索，减小时间复杂度。创建一个循环更新的tocheck(相当于一个队列)，

依次取出tocheck中元素，与lst中可用的平方项比较，将可能组成tocheck中元素的lst中的所有可能元素取出，添加到temp中(temp.add(x-y))，更新tocheck，最终获得结果。