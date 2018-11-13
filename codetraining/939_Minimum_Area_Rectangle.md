#939_Minimum_Area_Rectangle

------

> - 问题
> - 代码
> - 思路

------

## 问题

 939.最小面积矩形

 

给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

 

如果没有任何矩形，就返回 0。

 

示例 1：

 

输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]

输出：4

示例 2：

 

输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

输出：2

 

提示：

 

1 <= points.length <= 500

0 <= points[i][0] <= 40000

0 <= points[i][1] <= 40000

所有的点都是不同的。

## 代码

```python
import collections
class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        s = set(map(tuple, points))
        dx = collections.defaultdict(list)
        dy = collections.defaultdict(list)
        for x,y in points:
            dx[x].append(y)
            dy[y].append(x)

        res = float('inf')
        for x in sorted(dx.keys()):
            for i in range(len(dx[x])):
                y1 = dx[x][i]
                for j in range(i+1, len(dx[x])):
                    y2 = dx[x][j]
                    for x1 in dy[y2]:
                        if x1 <= x: continue
                        if (x1, y1) in s:
                            res = min(res, abs(x-x1) * abs(y1-y2))

        return res if res != float('inf') else 0

if __name__ == "__main__":
    sl=Solution()
    points=[[1,1],[1,3],[3,1],[3,3],[2,2]]
    print(sl.minAreaRect(points))
```

## 思路

思路:

我们先用两个字典将所有的点按照横坐标和纵坐标记录下来

我们用dx[i]表示在x= i这条线上的所有点的纵坐标，用dy[i]表示在y=i这条线上所有点的纵坐标，那么对于示例1:，有：

dx = {1: [1,3], 2:[2], 3:[1,3]}

dy = {1: [1,3], 2:[2], 3:[1,3]}

 

我们如何去寻找矩形的四个点呢？

 

在dx中选定一个x

在dx[x]中选定两个不同的y，分别为y1,y2

在dy[y1]中找到一个x1，且 x1 != x

最后判断 x1,y2 是否存在于points当中。

若存在，计算面积

若不存在，go to step 1