#47 Permutations II

---

> * 问题
> * 代码
> * 思路

---

## 问题

全排列Ⅱ

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1, 1, 2]

输出:

[

​    [1, 1, 2],

​    [1, 2, 1],

​    [2, 1, 1]

]

## 代码

```python
import copy
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permuteRecursive(nums, 0, res)
        return res
    def permuteRecursive(self, nums, start, res):
        if start == len(nums) and nums not in res:
            temp = copy.deepcopy(nums)
            res.append(temp)
            return
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                self.permuteRecursive(nums, start+1, res)
                nums[start], nums[i] = nums[i], nums[start]
sl=Solution()
nums=[1,2,1]
res=[]
res=sl.permuteUnique(nums)
print(res)
```

## 思路

对全排列那道题稍加修改，在将nums加入res是添加是否存在于res中的判断，不存在则添加，存在则跳过。