#42 Trapping Rain Water

---

> * 问题
> * 代码
> * 思路

---

## 问题

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

![](./42trapping_rain_water.png)

示例:

输入: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

输出: 6

## 代码

```python
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        mx=0
        dp=[0]*len(height)
        for i in range(len(height)):
            dp[i]=mx
            mx=max(mx,height[i])
        mx=0
        i=len(height)-1
        while i>=0:
            dp[i]=min(mx,dp[i])
            mx=max(mx,height[i])
            if dp[i]>height[i]:
                res+=dp[i]-height[i]
            i-=1
        return res 
sl=Solution();
res=0;
height = [5, 2, 1, 2, 1, 5]
res=sl.trap(height)
print(res)
```

##思路

这种方法是基于动态规划Dynamic Programming的，我们维护一个一维的dp数组，这个DP算法需要遍历两遍数组，第一遍遍历dp[i]中存入i位置左边的最大值，然后开始第二遍遍历数组，第二次遍历时找右边最大值，然后和左边最大值比较取其中的较小值，然后跟当前值A[i]相比，如果大于当前值，则将差值存入结果