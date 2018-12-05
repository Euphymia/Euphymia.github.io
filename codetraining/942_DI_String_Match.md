#942_DI_String_Match

------

> - 问题
> - 代码
> - 思路

------

## 问题

 \942. 增减字符串匹配

 

给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

 

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

 

如果 S[i] == "I"，那么 A[i] < A[i+1]

如果 S[i] == "D"，那么 A[i] > A[i+1]

 

 

示例 1：

 

输出："IDID"

输出：[0,4,1,3,2]

示例 2：

 

输出："III"

输出：[0,1,2,3]

示例 3：

 

输出："DDI"

输出：[3,2,0,1]

 

 

提示：

 

1 <= S.length <= 1000

S 只包含字符 "I" 或 "D"。

## 代码

```python
class Solution:
    def diStringMatch1(self, S):
        left = right = 0
        res = [0]
        for i in S:
            if i == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [i - left for i in res]
    def diStringMatch2(self, S):
        res = list(range(len(S) + 1))
        for i, s in enumerate(S):
            if s == 'I' and res[i] > res[i+1] or s == 'D' and res[i] < res[i+1]:
                res[i:] = res[i:][::-1]
        return res     
    def diStringMatch(self, S):
        cur_list=[i for i in range(len(S)+1)]
        res=[]
        for i in S:
            if i=='I':
                res.append(cur_list.pop(0))
            else:
                res.append(cur_list.pop())
        res.append(cur_list[0])
        return res

if __name__ == "__main__":
    sl=Solution()
    S = "DDI"
    print(sl.diStringMatch(S))
```

## 思路

思路：

diStringMatch2，第二个方法很好理解，先创建一个0-lenght(S)+1的数组res，

然后开始遍历S，如果遇到不满足条件的位置，就令数组res从当前位置一直到最后逆序，这样就肯定符合条件了，便利到最后即可

方法一：

极为巧妙！ left和right记录S中降低和增加的个数，并构建一个数组res,我们最后的数组是令res中每个数减去减少的个数left，

首先第一个数是后面减的数目，即left，然后之后的结果是每遇到一个'D'就令其在上次'D'的基础上减一，遇到'I'，则在上一次的基础上加一。

第三种方法：

创建待选数组cur_list

遇到I添加一个cur_list中最小的，遇到D添加一个cur_list中最大的