# 75_Sort_Colors

---

> * 问题
> * 代码
> * 思路

---

## 问题

\75. 分类颜色

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:

不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]

输出: [0,0,1,1,2,2]

进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。

首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。

你能想出一个仅使用常数空间的一趟扫描算法吗？

注意这里的in-place是指使用O(1)的额外空间

## 代码

```python

class Solution:
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 计数排序
        colorNum=[0]*3
        result=[]
        for i in nums:
            colorNum[i]+=1
        for i in range(len(colorNum)):
            result.extend([i]*colorNum[i])
        return result
    def sortColors2(self,nums):
        # 使用两个指针
        left=0
        right=len(nums)-1
        i=0
        while i<=right:
            if nums[i]==0:
                nums[i],nums[left]=nums[left],nums[i]
                left+=1
            elif nums[i]==2:
                nums[i],nums[right]=nums[right],nums[i]
                i-=1
                right-=1
            i+=1
if __name__=="__main__":
    sl=Solution()
    nums=[2,0,1]
    sl.sortColors2(nums)
    print(nums)
```



##思路

思路1

这道题的本质还是一道排序的题，题目中给出提示说可以用计数排序，需要遍历数组两遍，那么先来看这种方法，因为数组中只有三个不同的元素，所以实现起来很容易。

 

\- 首先遍历一遍原数组，分别记录0,1,2的个数

\- 然后更新原数组，按个数分别赋上0，1，2

 

思路2

我需要用双指针来做，分别从原数组的首尾往中心移动。

 

\- 定义red指针指向开头位置，blue指针指向末尾位置

 

\- 从头开始遍历原数组，如果遇到0，则交换该值和red指针指向的值，并将red指针后移一位。若遇到2，则交换该值和blue指针指向的值，并将blue指针前移一位。若遇到1，则继续遍历。