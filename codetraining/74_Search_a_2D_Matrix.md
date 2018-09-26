# 74_Search_a_2D_Matrix

---

> * 问题
> * 代码
> * 思路

---

## 问题

\74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

 

每行中的整数从左到右按升序排列。

每行的第一个整数大于前一行的最后一个整数。

示例 1:

 

输入:

matrix = [

  [1,   3,  5,  7],

  [10, 11, 16, 20],

  [23, 30, 34, 50]

]

target = 3

输出: true

示例 2:

 

输入:

matrix = [

  [1,   3,  5,  7],

  [10, 11, 16, 20],

  [23, 30, 34, 50]

]

target = 13

输出: false

##代码

```python
class Solution:
    def searchMatrix(self, matrix, target):
            if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

if __name__=="__main__":
    sl=Solution()
    result=sl.searchMatrix([
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ],13)
    print(result)
```



##思路

由于给的矩阵是有序的，所以很自然的想到要用二分查找法，直接将这个二维数组看成一个已经排序好的数列，使用二分查找即可。 