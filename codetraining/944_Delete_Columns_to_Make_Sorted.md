#944_Delete_Columns_to_Make_Sorted

------

> - 问题
> - 代码
> - 思路

------

## 问题

 \944. 删除列以使之有序

 

给出由 N 个小写字母串组成的数组 A，所有小写字母串的长度都相同。

 

现在，我们可以选择任何一组删除索引，对于每个字符串，我们将删除这些索引中的所有字符。

 

举个例子，如果字符串为 "abcdef"，且删除索引是 {0, 2, 3}，那么删除之后的最终字符串为 "bef"。

 

假设我们选择了一组删除索引 D，在执行删除操作之后，A 中剩余的每一列都是有序的。

 

形式上，第 c 列为 [A[0][c], A[1][c], ..., A[A.length-1][c]]

 

返回 D.length 的最小可能值。

 

 

 

示例 1：

 

输入：["cba","daf","ghi"]

输出：1

示例 2：

 

输入：["a","b"]

输出：0

示例 3：

 

输入：["zyx","wvu","tsr"]

输出：3

 

 

提示：

 

1 <= A.length <= 100

1 <= A[i].length <= 1000

## 代码

```python
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = 0
        for i in range(len(A[0])):
            for j in range(len(A)-1):
                if A[j][i] > A[j+1][i]:
                    s += 1
                    break
        return s

if __name__ == "__main__":
    sl=Solution()
    A=["cba","daf","ghi"]
    print(sl.minDeletionSize(A))
```

## 思路

思路：

这道题描述很差劲，题意为，删除哪几列，使得最后的数组有序，有序是指每列有序，所以只需找出所有的无序列即可