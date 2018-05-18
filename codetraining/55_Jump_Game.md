#55 Jump Game

---

> * 问题
> * 代码
> * 思路

---

## 问题

跳跃游戏

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2, 3, 1, 1, 4]

输出: true

解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:

输入: [3, 2, 1, 0, 4]

输出: false

解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

## 代码

```python
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach=0
        for i in range(len(nums)):
            if i>maxreach or maxreach>=len(nums)-1:
                break
            maxreach=max(maxreach,i+nums[i])
        return maxreach>=len(nums)-1

def test():
    sl=Solution()
    nums=[3,2,1,0,4]
    print(sl.canJump(nums))

if __name__=='__main__':
    test()
```

## 思路

本题就是求输入列表最多可以不间断跳到哪个位置，只要比最后一个远即可，不能中断。