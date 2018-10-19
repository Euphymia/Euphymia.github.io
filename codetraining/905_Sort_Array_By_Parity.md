#905_Sort_Array_By_Parity

------

> - 问题
> - 代码
> - 思路

## 问题

\905. Sort Array By Parity

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

 

You may return any answer array that satisfies this condition.

 

 

Example 1:

 

Input: [3, 1, 2, 4]

Output: [2, 4, 3, 1]

The outputs[4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3] would also be accepted.

 

给定一个A非负整数数组，返回一个由所有偶数元素组成的数组A，后跟所有奇数元素A。

 

您可以返回满足此条件的任何答案数组。

Note:

 

1 <= A.length <= 5000

0 <= A[i] <= 5000

## 代码

```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddlist=[]
        evenlist=[]
        for i in A:
            if i%2!=0:
                oddlist.append(i)
            else:
                evenlist.append(i)
        evenlist.extend(oddlist)
        return evenlist
if __name__=="__main__":
    sl=Solution()
    a=[3,1,2,4]
    print(sl.sortArrayByParity(a))
```

## 思路

思路：

很简单，将输入的数组中偶数，奇数各组成一个新数组，最后拼接起来即可。

注意，列表的append，extend方法没有返回值，不能直接return a.append(b)