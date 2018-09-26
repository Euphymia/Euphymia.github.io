#64_Minimum_Path_Sum.py

---

> * 问题
> * 代码
> * 思路

---

## 问题

64. 最小路径和

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:

[

  [1,3,1],

  [1,5,1],

  [4,2,1]

]

输出: 7

解释: 因为路径 1→3→1→1→1 的总和最小。

## 代码

```python
import numpy as np
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp=list(np.zeros((len(grid),len(grid[0]))))
        dp = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(len(grid)):
            if i==0:
                continue
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for i in range(len(grid[0])):
            if i==0:
                continue
            dp[0][i]=grid[0][i]+dp[0][i-1]
        i,j=1,1
        while i<len(grid):
            j=1
            while j <len(grid[0]):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
                j+=1
            i+=1
        return dp[len(grid)-1][len(grid[0])-1]

if __name__=='__main__':
    sl=Solution()
    result=sl.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print(result)
```

## 思路

思路：用动态规划Dynamic Programming来做，这应该算是DP问题中比较简单的一类，我们维护一个二维的dp数组，其中dp[i][j]表示当前位置的最小路径和，递推式也容易写出来 dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1]), 反正难度不算大

 