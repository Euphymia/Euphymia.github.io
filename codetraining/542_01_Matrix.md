#542_01_Matrix

------

> - 问题
> - 代码
> - 思路

## 问题

\542. 01 矩阵

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

 

两个相邻元素间的距离为 1 。

 

示例 1:

输入:

 

0 0 0

0 1 0

0 0 0

输出:

 

0 0 0

0 1 0

0 0 0

示例 2:

输入:

 

0 0 0

0 1 0

1 1 1

输出:

 

0 0 0

0 1 0

1 2 1

注意:

 

给定矩阵的元素个数不超过 10000。

给定矩阵中至少有一个元素是 0。

矩阵中的元素只在四个方向上相邻: 上、下、左、右。

## 代码

```python
import collections


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        Q = collections.deque([])
        visited = set()
        # 初始化队列，将所有起始点加入
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        # 标准bfs写法，将相邻节点加入队列
        while Q:
            i, j = Q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # 不出界 and 不走回头路
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    # visited一定要在这里添加，否则产生大量重复计算
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix

if __name__ == "__main__":
    sl = Solution()
    A = [[0 ,0, 0],[0, 1, 0],[1, 1, 1]] 
    print(sl.updateMatrix(A))
```

## 思路

思路

对于这道题，怎么找bfs的起始点呢，我们可能最初想到的是对每一个1都进行一次bfs遍历，去寻找与他最近的0的位置，但这样显然会超时，因为当1都聚集在一起的时候会有大量重复计算。

换个思路，既然1不行，那0行吗，以单个的0肯定不行，因为这个0找到的最近的1，并不一定是最短的，还得计算别的0然后来比较，所以还是得有大量重复计算和比较。

既然起始点找单个不行，我们可以找多个，我们将所有的0作为起始点，去找所有最后res[i][j] = 1的点，然后将res = 1的点作为起始点，去找所有最后res[i][j] = 2的点，以此类推。

 