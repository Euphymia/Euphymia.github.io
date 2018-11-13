#934_Shortest_Bridge

------

> - 问题
> - 代码
> - 思路

------

## 问题

 934.最短的桥

在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。

返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。）

示例 1：

输入：[[0,1],[1,0]]

输出：1

示例 2：

输入：[[0,1,0],[0,0,0],[0,0,1]]

输出：2

示例 3：

输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

输出：1

提示：

1 <= A.length = A[0].length <= 100

A[i][j] == 0 或 A[i][j] == 1

## 代码

```python
class Solution:
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, bfs = len(A), 0, []
        dfs(*first())
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new


if __name__=="__main__":
    sl=Solution()
    A=[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(sl.shortestBridge(A))
```

## 思路

想法很简单。从first()得到第1岛的根，我们对根进行dfs找到第一个岛所有的位置(设置为-1)，并将索引添加到bfs，我们对第一个岛屿进行广度优先搜索，直到到达第二个岛(搜索到1)，如果没到(搜索到0)就扩展bfs，进行下一轮搜索。

最后到达其他岛时返回步数，