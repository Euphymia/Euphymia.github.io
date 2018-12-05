#120_Triangle

------

> - 问题
> - 代码
> - 思路

------

## 问题

 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

 

例如，给定三角形：

 

[

​     [2],

​    [3,4],

   [6,5,7],

  [4,1,8,3]

]

自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 

说明：

 

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

## 代码

```python
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length=len(triangle)
        row_len=1
        dp=[0]*length
        dp[0]=triangle[0][0]
        for i in range(len(triangle)-1):
            row_len+=1
            row_temp=[i for i in dp]
            for j in range(row_len):
                if 0<j<row_len-1:
                    dp[j]=triangle[i+1][j] + min(row_temp[j],row_temp[j-1])
                elif j==row_len-1:
                    dp[j]=triangle[i+1][j] + row_temp[j-1]
                else:
                    dp[j]=triangle[i+1][j] + row_temp[j]
        return min(dp)
if __name__ == "__main__":
    sl=Solution()
    triangle=[
            [2],
            [3,4],
            [6,5,7],
            [4,1,8,3]
        ]
    print(sl.minimumTotal(triangle))
```

## 思路

思路：

标桩的动态规划，这里使用的是从上到下的顺序(也可以从下到上)，创建dp数组，每次找到最有的解，即dp[j]=triangle[i+1][j] + min(row_temp[j],row_temp[j-1])。

最后的dp中最小的就是我们要的。