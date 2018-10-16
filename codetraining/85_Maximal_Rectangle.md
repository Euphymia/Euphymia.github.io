# 85_Maximal_Rectangle

---

> * 问题
> * 代码
> * 思路

---

## 问题

85. 最大矩形

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:

[

  ["1","0","1","0","0"],

  ["1","0","1","1","1"],

  ["1","1","1","1","1"],

  ["1","0","0","1","0"]

]

输出: 6

## 代码

```python
class Solution:
    def largestRectangleArea(self, heights):
        s = []
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            left_index = i
            while len(s) > 0 and s[-1][0] >= heights[i]:    
                last = s.pop()
                # left_index这里用来记录本次遇到的低矩形可向前一直勾勒到第几的矩形，并在本次while循环后保存起来，便于下次比较
                left_index = last[1]
                ans = max(ans, heights[i] * (i + 1 - last[1]))
                ans = max(ans, last[0] * (i - last[1]))
            s.append((heights[i], left_index))
        return ans
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        area = 0
        for row in matrix:
            for col_num, item in enumerate(row):
                heights[col_num] = heights[col_num] + 1 if item == '1' else 0
            area = max(area, self.largestRectangleArea(heights))
            # print(heights)
        return area

if __name__=='__main__':
    sl=Solution()
    matrixrec=[
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
    res=sl.maximalRectangle(matrixrec)
    print(res)
```



##思路.

将二维矩阵一层一层分开，第一层，前两层....，并视为以第二层，第三层为底的矩形，然后看做是如84题的求最大矩形面积，调用84的方法即可解题 