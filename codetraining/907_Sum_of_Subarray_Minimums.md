#907_Sum_of_Subarray_Minimums

------

> - 问题
> - 代码
> - 思路

## 问题

907.子阵列最小值之和

给定整数数组A，求总和min(B)，其中B范围超过每（连续的）子阵列A。

由于答案可能很大，因此返回答案模数10 ^ 9 + 7。

例1：

输入：[3, 1, 2, 4]

输出：17

说明：子阵列为[3]，[1]，[2]，[4]，[3, 1]，[1, 2]，[2, 4]，[3, 1, 2]，[1, 2, 4]，[3, 1, 2, 4]。

​    最小值为3, 1, 2, 4, 1, 1, 2, 1, 1, 1。总和为17。

​    注意：

 

​    1 <= A.length <= 30000

​    1 <= A[i] <= 30000

## 代码

```python
# class Solution:
#     def sumSubarrayMins(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         res=sum(A)
#         i=2
#         while i<len(A)+1:
#             j=0
#             while j+i<=len(A):
#                 res+=min(A[j:j+i])
#                 j+=1
#             i+=1
#         return res%(10**9+7)
class Solution:
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod
if __name__ == "__main__":
    sl = Solution()
    a = [3, 1, 2, 4]
    print(sl.sumSubarrayMins(a))
```

## 思路

思路：

这个思路很巧妙。找到每个位置的数字为最小值的可能存在的数量

方法是以第i个数字为中心，向左连续找比它大的数字的个数，再向右找比它大的数字的个数，将这两个数相乘即得到以该位置为最小值的可能存在的数量。