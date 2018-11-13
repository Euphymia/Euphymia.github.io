#930_Binary_Subarrays_With_Sum

------

> - 问题
> - 代码
> - 思路

------

## 问题

 930.和相同的二元子数组

 

在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

 

示例：

 

输入：A = [1, 0, 1, 0, 1], S = 2

输出：4

解释：

如下面黑体所示，有 4 个满足题目要求的子数组(连续)：

[1, 0, 1, 0, 1]

[1, 0, 1, 0, 1]

[1, 0, 1, 0, 1]

[1, 0, 1, 0, 1]

 

提示：

 

A.length <= 30000

0 <= S <= A.length

A[i] 为 0 或 1

## 代码

```python
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        res=0
        cur_num=0
        left=0
        for ind in range(len(A)):
            cur_num+=A[ind]
            if cur_num==S:
                res+=1
                temp=left
                while temp < ind and A[temp] == 0:
                    temp+=1
                    res += 1
            elif cur_num==S+1 :
                while left < len(A) and A[left] == 0:
                    left += 1
                if left<ind :
                    cur_num-=1
                    left+=1
                    res+=1
                elif left == ind:
                    cur_num-=1
                    left+=1
                temp = left
                while temp < ind and A[temp] == 0:
                    temp += 1
                    res += 1
        return res



if __name__=="__main__":
    sl=Solution()
    A = [1, 0, 1, 0, 1]
    S = 2
    print(sl.numSubarraysWithSum(A,S))
```

## 思路

思路：

并不好的一个思路，设置一个left表示窗口的左侧，遍历数组A，统计当前的总和cur_num,如果等于S，计算出所有可能的自己数，即如果当前窗口的左侧有多少0，就有多少可能的组合。

如果大于S，先将left向右移动到1为止，因为都是不合格的，然后删除一个1，如果删除的1就是当前ind的值，不令res+1, 否则+1，然后在统计当前窗口的左侧有多少0，这样就又有多少可能的组合，

最后返回res

 