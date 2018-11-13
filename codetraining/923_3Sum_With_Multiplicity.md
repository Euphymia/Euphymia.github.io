# 923_3Sum_With_Multiplicity

------

> - 问题
> - 代码
> - 思路

------

## 问题

 923.三数之和的多种可能

 

给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的元组 i, j, k 的数量。

 

由于结果会非常大，请返回 结果除以 10 ^ 9 + 7 的余数。

 

示例 1：

 

输入：A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target = 8

输出：20

解释：

按值枚举（A[i]，A[j]，A[k]）：

(1, 2, 5) 出现 8 次；

(1, 3, 4) 出现 8 次；

(2, 2, 4) 出现 2 次；

(2, 3, 3) 出现 2 次。

示例 2：

 

输入：A = [1, 1, 2, 2, 2, 2], target = 5

输出：12

解释：

A[i] = 1，A[j] = A[k] = 2 出现 12 次：

我们从[1, 1] 中选择一个 1，有 2 种情况，

从[2, 2, 2, 2] 中选出两个 2，有 6 种情况。

 

提示：

 

3 <= A.length <= 3000

0 <= A[i] <= 100

0 <= target <= 300

## 代码

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        hash = {}
        res = 0
        MOD = 10**9 + 7
        for i, val in enumerate(A):
            res = res + hash.get(target - val, 0)
            for j in range(i):
                temp = A[j] + val
                hash[temp] = hash.get(temp, 0) + 1
        return res
    

if __name__=="__main__":
    sl=Solution()
    A = [1, 1, 2, 2, 2, 2]
    print(sl.threeSumMulti(A,5))
```

## 思路

思路：

非常巧妙，使用hash用于保存可能存在的两数之和。将3sum转为target-val的2sum问题，每次res增加的都是当前val与它之前的任意两个

和为target-val的可能出现的组合个数，所以并不会重复