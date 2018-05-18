#53 Maximum Subarray

---

> * 问题
> * 代码
> * 思路

---

## 问题

最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4],

输出: 6

解释: 连续子数组[4, -1, 2, 1] 的和最大，为 6。

## 代码

```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int 
        """
        res=-2**31
        cursum=0
        for i in range(len(nums)):
            cursum=max(cursum+nums[i],nums[i])
            res=max(cursum,res)
        return res

def test():
    sl=Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sl.maxSubArray(nums))


if __name__=='__main__':
    test()
```

