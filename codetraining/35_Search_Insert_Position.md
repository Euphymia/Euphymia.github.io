#35 Search Insert Position

---

> * 问题
> * 代码

---

## 问题

搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

##代码

```python
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            print(mid)
            if nums[mid]==target: return mid
            elif nums[mid]<target: start=mid+1
            else: end=mid-1
        return (start+end)//2+1
sl=Solution();
nums = [1, 3, 5, 6]
target=2
res=sl.searchInsert(nums,target)
print(res)
```

