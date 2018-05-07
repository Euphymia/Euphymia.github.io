#34 Search for a Range

---

> * 问题
> * 代码
> * python运算符

---

## 问题

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。你的算法时间复杂度必须是 O(log n) 级别。如果数组中不存在目标值，返回[-1, -1]。

## 代码

```python
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(int)((start+end)/2)
            if nums[mid]==target:
                start=end=mid
                while start>=0 and nums[start]==target:
                    start-=1
                while end<=len(nums)-1 and nums[end]==target:
                    end+=1
                return [start+1,end-1]
            elif nums[mid]<target:
                start=mid+1
            else :
                end=mid-1
        return [-1,-1]
sl=Solution();
nums=[5,7,7,8,8,10]
target=6
res=sl.searchRange(nums,target)
print(res)
```

## python运算符

```python
数学运算符

// 运算符

取整除 - 返回商的整数部分

**运算符

幂 - 返回x的y次幂

%运算符

取余

比较运算符

<>比较运算符 

不等于 - 比较两个对象是否不相等

Python位运算符

按位运算符是把数字看作二进制来进行计算的。

&   

按位与运算符：参与运算的两个值, 如果两个相应位都为1, 则该位的结果为1, 否则为0

|   

按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。

^   

按位异或运算符：当两对应的二进位相异时，结果为1

<< 

左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。

>>  

右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数

Python成员运算符

in 

如果在指定的序列中找到值返回 True，否则返回 False。

not in

如果在指定的序列中没有找到值返回 True，否则返回 False。
```

