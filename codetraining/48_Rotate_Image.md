#48 Rotate Image

---

> * 问题
> * 代码
> * 思路

---

## 问题

旋转图像

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 

[

  [1,2,3],

  [4,5,6],

  [7,8,9]

],

原地旋转输入矩阵，使其变为:

[

  [7,4,1],

  [8,5,2],

  [9,6,3]

]

示例 2:

给定 matrix =

[

  [ 5, 1, 9,11],

  [ 2, 4, 8,10],

  [13, 3, 6, 7],

  [15,14,12,16]

], 

原地旋转输入矩阵，使其变为:

[

  [15,13, 2, 5],

  [14, 3, 4, 1],

  [12, 6, 8, 9],

  [16, 7,10,11]

]

## 代码

```python
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        j,i=0,0

        while i<n:
            j=i+1
            while j<n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j+=1
            i+=1
        i,j=0,0
        while i<n:
            j=0
            while j<n/2:
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
                j+=1
            i+=1
def test():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sl=Solution()
    sl.rotate(matrix)
    print(matrix)

if __name__ == '__main__':
    test()
```

## 思路

首先以从对角线为轴翻转，然后再以x轴中线上下翻转即可得到结果