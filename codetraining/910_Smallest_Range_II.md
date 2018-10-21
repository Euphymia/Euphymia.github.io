# 910_Smallest_Range_II

------

> - 问题
> - 代码
> - 思路

------

## 问题

 910.最小差值 II

给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

示例 1：

输入：A = [1], K = 0

输出：0

解释：B = [1]

示例 2：

输入：A = [0, 10], K = 2

输出：6

解释：B = [2, 8]

示例 3：

输入：A = [1, 3, 6], K = 3

输出：3

解释：B = [4, 6, 3]

提示：

1 <= A.length <= 10000

0 <= A[i] <= 10000

0 <= K <= 10000

## 代码

```python
class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        res = A[-1] - A[0]
        maxA, minA = A[-1], A[0]+2*K
        for i in range(len(A) - 1):
            big = max(maxA, A[i] + 2 * K)
            small = min(A[i + 1], minA)
            res = min(res, big - small)
        return res


if __name__ == "__main__":
    sl = Solution()
    A = A = [1, 3, 6]
    print(sl.smallestRangeII(A, 3))
```

## 思路

思路：

精妙！先排序，计算最大差值(随便设置了一个最大值最小值同时加或减K时的值，用于更新)。

这里用A[i]+2*K和A[i]表示对A[i]进行了+K或-K。

遍历数组(从第一个到倒数第二个)

big：将第i个数的最大值(A[i]+2*K)与初始的最大值maxA比较，得到大的

small：将第i+1个数本身(表示已-K)，与minA比较，得到小的。

保存产生的最小差值。