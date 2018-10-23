#926_Flip_String_to_Monotone_Increasing

------

> - 问题
> - 代码
> - 思路

------

## 问题

 926.将字符串翻转到单调递增

 

如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。

 

我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。

 

返回使 S 单调递增的最小翻转次数。

 

 

示例 1：

 

输入："00110"

输出：1

解释：我们翻转最后一位得到 00111.

示例 2：

 

输入："010110"

输出：2

解释：我们翻转得到 011111，或者是 000111。

示例 3：

 

输入："00011000"

输出：2

解释：我们翻转得到 00000000。

 

 

提示：

 

1 <= S.length <= 20000

S 中只包含字符 '0' 和 '1'

## 代码

```python
class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        len_S=len(S)-1
        left=[0]
        one_count=0
        right=[0]
        zero_count=0
        i=1
        while i<=len_S:
            if S[i-1]=='1':
                one_count+=1
            if S[len_S-i+1]=='0':
                zero_count+=1
            left.append(one_count)
            right.append(zero_count)
            i+=1
        # 经测试这种方法比较慢
        # res=len_S
        # for i in range(len(left)):
        #     res=min(res,left[i]+right[len_S-i])
        # return res
        res=[]
        for i in range(len(left)):
            res.append(left[i]+right[len_S-i])
        return min(res)


if __name__ == "__main__":
    sl = Solution()
    S = "010110"
    print(sl.minFlipsMonoIncr(S))
```

## 思路

思路：

我们可以通过统计一个点之前有多少个1以及之后有多少个0算出需要翻转的次数。

这里初始化的两个数列，left记录左边有多少个1，right记录右边有多少个0.统计的过程就是从两头开始遍历，记录遇到的1和0的个数，添加到left和right数组中。

将left中的数与right中的数(倒序，因为这里的数是从后向前算的)相加，最后返回最小的即可。