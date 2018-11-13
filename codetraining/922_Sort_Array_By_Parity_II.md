#922_Sort_Array_By_Parity_II

------

> - 问题
> - 代码
> - 思路

------

## 问题

 922.按奇偶排序数组 II

给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

示例：

输入：[4, 2, 5, 7]

输出：[4, 5, 2, 7]

解释：[4, 7, 2, 5]，[2, 5, 4, 7]，[2, 7, 4, 5] 也会被接受。

提示：

2 <= A.length <= 20000

A.length % 2 == 0

0 <= A[i] <= 1000

## 代码

```python
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddlist=[i for i in A if(i%2!=0)]
        evenlist=[i for i in A if(i%2==0)]
        res=[]
        for i,j in zip(oddlist,evenlist):
            res.append(j)
            res.append(i)
        return res
if __name__=="__main__":
    sl=Solution()
    A = [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]
    print(sl.sortArrayByParityII(A))
```

## 思路

思路：

很简单，创建两个数组，一个保存奇数，一个保存偶数，然后将两个数组按顺序合并