#63_Unique_Paths_II

---

> * 问题
> * 代码
> * 思路

---

## 问题

63.独特的道路II

机器人位于一个m x n网格的左上角（在下图中标记为“开始”）。

机器人只能随时向下或向右移动。机器人正在尝试到达网格的右下角（在下图中标记为“完成”）。

现在考虑是否有一些障碍物被添加到网格中。将有多少独特的路径？

注意： m和n最多为100。

例1：

输入：

 [

​     [0, 0, 0]

​     [0, 1, 0]

​     [0, 0, 0]

 ]

输出： 2

 说明：

在上面的3x3网格中间有一个障碍。

有两种方法可以触及右下角：

1.右键 - >右键 - >下 - >下键

2.向下 - >向下 - >向右 - >向右

## 代码

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width = len(obstacleGrid[0])
        dp = [0]*width
        dp[0]=1
        for row in obstacleGrid:
            j=0
            while j<width:
                if row[j]==1:
                    dp[j] = 0
                elif j>0:
                    dp[j]+=dp[j-1]                
                j+=1
        return dp[width-1]

if __name__=="__main__":
    sl=Solution()
    result=sl.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(result)
```

## 思路

与unique_path类似，使用一个一维数组记录所有可能的路径数，遇到一行中有1时，将dp数组在该位置置零，表示此路之前的路均不通，重新计算。