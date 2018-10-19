#896_Monotonic_Array

------

> - 问题
> - 代码
> - 思路

## 问题

\896. 单调数列

如果数组是单调递增或单调递减的，那么它是单调的。

 

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i] > = A[j]，那么数组 A 是单调递减的。

 

当给定的数组 A 是单调数组时返回 true，否则返回 false。

 

 

示例 1：

 

输入：[1, 2, 2, 3]

输出：true

示例 2：

 

输入：[6, 5, 4, 4]

输出：true

示例 3：

 

输入：[1, 3, 2]

输出：false

示例 4：

 

输入：[1, 2, 4, 5]

输出：true

示例 5：

 

输入：[1, 1, 1]

输出：true

 

 

提示：

 

1 <= A.length <= 50000

-100000 <= A[i] <= 100000

## 代码

```python
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag=0
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                continue
            if flag==0:
                if A[i]>A[i+1]:
                    flag=1
                else:
                    flag=2
            elif flag==1:
                if A[i]>=A[i+1]:
                    continue
                else:
                    return False
            else:
                if A[i]<A[i+1]:
                    continue
                else:
                    return False
        return True

if __name__=="__main__":
    sl=Solution()
    A = [1, 3, 2]
    print(sl.isMonotonic(A))
```

## 思路

很简单，设置几个flag，判断即可。