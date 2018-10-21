# 915_Partition_Array_into_Disjoint_Intervals

------

> - 问题
> - 代码
> - 思路

---

## 问题

 915.分割数组

给定一个数组 A，将其划分为两个不相交的连续子数组 left 和 right， 使得：

 

left 中的每个元素都小于或等于 right 中的每个元素。

left 和 right 都是非空的。

left 要尽可能小。

在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。

 

 

示例 1：

 

输入：[5, 0, 3, 8, 6]

输出：3

解释：left = [5, 0, 3]，right = [8, 6]

示例 2：

 

输入：[1, 1, 1, 0, 6, 12]

输出：4

解释：left = [1, 1, 1, 0]，right = [6, 12]

 

 

提示：

 

2 <= A.length <= 30000

0 <= A[i] <= 10 ^ 6

可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。

## 代码

```python
class Solution:
    def mypartitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tempA=A
        newA = list(set(tempA))
        newA.sort()
        res=0
        while True:
            # temp=[idx for idx, e in enumerate(tempA) if e == newA[0]]
            idx=tempA.index(newA[0])+1
            # for j in temp:
            # idx=j+1
            if idx == len(tempA)+1:
                return idx+res-1
            elif max(A[0:idx+res])<=min(A[idx+res:]):
                return idx+res
            tempA=tempA[idx:]
            res+=idx
            newA = list(set(tempA))
            newA.sort()

    def partitionDisjoint(self, A):
        disjoint = 0
        v = A[disjoint]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                disjoint = i
                v = max_so_far
        return disjoint + 1
if __name__ == "__main__":
    sl = Solution()
    A = [5, 0, 3, 8, 6]
    A2 = [1, 1, 1, 0, 6, 12]
    A3 = [32, 57, 24, 19, 0, 24, 49, 67, 87, 87]
    print(sl.partitionDisjoint(A3))
```

## 思路

思路：

我的思路，将数组排序，找到最小的数所在的位置，判断左右两边是否符合条件，如果不符合，将数组缩小为该位置的有半部分(左方一定不符合)，

注意记录res，保存已近产出的数组个数，便于得出结果所在的位置。继续循环，直到出现符合条件的位置。

 

更好的思路，disjoint，记录应该划分的位置，v，保存符合条件的最大的数，max_so_far，记录到目前为止最大的数，遍历一次数组，

记录到目前为止出现的最大的数，如果本次循环出现的数比v小，则更新disjoint和v，继续向下循环，最终返回disjoint+1

 