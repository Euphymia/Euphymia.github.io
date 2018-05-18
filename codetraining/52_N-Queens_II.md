#52 N-Queens II

---

> * 问题
> * 代码
> * 思路

---

## 问题

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4

输出: 2

解释: 4 皇后问题存在如下两个不同的解法。

[

​    [".Q..",  // 解法 1

​    "...Q",

​    "Q...",

​    "..Q."],

​    ["..Q.",  // 解法 2

​        "Q...",

​        "...Q",

​        ".Q.."]

]

##代码

```python
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        pos = [-1]*n
        self.solveNQueensDFS(res, pos, 0)
        return len(res)

    def solveNQueensDFS(self, res, pos, row):
        n = len(pos)
        if row == n:
            out = ['.'*n]*n
            for i in range(n):
                newlist = list(out[i])
                newlist[pos[i]] = "Q"
                newlist = "".join(newlist)
                out[i] = newlist
            res.append(out)
            return
        for col in range(0, n):
            if self.isvalid(col, row, pos):
                pos[col] = row
                self.solveNQueensDFS(res, pos, row+1)
                pos[col] = -1

    def isvalid(self, col, row, pos):
        if pos[col] != -1:
            return False
        for i in range(1, row+1):
            if (col-i) >= 0 and pos[col-i] == row-i:
                return False
            if (col+i) < len(pos) and pos[col+i] == row-i:
                return False
        return True

def test():
    sl=Solution()
    print(sl.totalNQueens(8))

if __name__=='__main__':
    test()
```

## 思路 

思路与N皇后一样