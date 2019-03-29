#1021 最佳观光对 

------

> - 问题
> - 代码
> - 思路

------

## 问题

 给定一组A正整数，A[i]代表i第一个观光景点的价值，以及两个观光景点，i并且 它们之间j 有距离j - i。

 

 一对（）观光景点的得分i < j是（A[i] + A[j] + i - j)：观光景点的值的总和减去它们之间的距离。

返回一对观光景点的最高分。

例1：

输入：[8,1,5,2,6] 

输出：11

 说明： i = 0，j = 2，A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

注意：

2 <= A.length <= 50000

1 <= A[i] <= 1000

## 代码

```python
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # 分为两部分：A [i] + i 和 A [j] -j
        curmax = A[0]
        resmax = A[0]
        for i in range(1,len(A)):
            resmax = max(resmax,curmax+A[i]-i)
            curmax = max(curmax,A[i]+i)
        return resmax
```

## 思路

目标是跟踪：

 

到目前为止最大值并将其添加到cur_cell并保持最大结果

这里，max_so_far包含：A [i] + i

原始给定公式：A [i] + A [j] + i - j

 

分为两部分：A [i] + i 和 A [j] -j

保持到目前为止看到的元素中第一部分的MAX_VALUE

将当前元素添加到max_so_far并检查结果是否正在更改

此外，不断更新每一步的max_so_far