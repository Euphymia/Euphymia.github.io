#931_Minimum_Falling_Path_Sum

------

> - 问题
> - 代码
> - 思路

------

## 问题

 931.下降路径最小和

 

给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

 

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

 

示例：

 

输入：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

输出：12

解释：

可能的下降路径有：

[1, 4, 7], [1, 4, 8], [1, 5, 7], [1, 5, 8], [1, 5, 9]

[2, 4, 7], [2, 4, 8], [2, 5, 7], [2, 5, 8], [2, 5, 9], [2, 6, 8], [2, 6, 9]

[3, 5, 7], [3, 5, 8], [3, 5, 9], [3, 6, 8], [3, 6, 9]

和最小的下降路径是[1, 4, 7]，所以答案是 12。

 

提示：

 

1 <= A.length == A[0].length <= 100

-100 <= A[i][j] <= 100

 

## 代码

```python
class Solution(object):
    def minFallingPathSum(self, A):
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        # 初始化
        for j in range(n):
            dp[n-1][j] = A[n-1][j]
        # 懒得用技巧缩短代码了，这种测试直接写才是最快的
        for i in range(n-2, -1, -1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                elif j == n-1:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j])
                else:
                    dp[i][j] = A[i][j] + \
                        min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        return min(dp[0])

if __name__=="__main__":
    sl=Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sl.minFallingPathSum(A))
```

## 思路

我们从下至上分析，定义dp[i][j]表示从(i, j)这个点出发，达到最底层的最小代价。

显然，我们所求的答案就是min(dp[0])。

那么有dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])

 

初始化最后一行，dp[n-1] = A[n-1]！