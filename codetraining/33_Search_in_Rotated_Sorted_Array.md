#33 Search in Rotated Sorted Array

---

> * 问题
> * 代码
> * 思路

---

## 问题

// 问题

// 搜索旋转排序数组

// 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

// ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

// 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

// 你可以假设数组中不存在重复的元素。

// 你的算法时间复杂度必须是 O(log n) 级别。

// 示例 1:

// 输入: nums = [4,5,6,7,0,1,2], target = 0

// 输出: 4

// 示例 2:

// 输入: nums = [4,5,6,7,0,1,2], target = 3

// 输出: -1

## 代码

```c++
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[start]<=nums[mid]:
                if nums[start]<=target<=nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<=target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
sl=Solution()
nums=[4,5,6,7,1,2,3]
target=1
res=sl.search(nums,target)
print(res)
```

## 思路

如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了。