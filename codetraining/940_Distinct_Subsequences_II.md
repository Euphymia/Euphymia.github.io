#940_Distinct_Subsequences_II

------

> - 问题
> - 代码
> - 思路

------

## 问题

 940.不同的子序列 II

给定一个字符串 S，计算 S 的不同非空子序列的个数。

 

因为结果可能很大，所以返回答案模 10^9 + 7.

 

示例 1：

 

输入："abc"

输出：7

解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

示例 2：

 

输入："aba"

输出：6

解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。

示例 3：

 

输入："aaa"

输出：3

解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

 

提示：

 

S 只包含小写字母。

1 <= S.length <= 2000

## 代码

```python
class Solution:
    def distinctSubseqII(self, S):
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)

if __name__ == "__main__":
    sl=Solution()
    S="abc"
    print(sl.distinctSubseqII(S))
```

## 思路

思路：

非常精妙！！

因为之前做过一道类似的题，我原来的思路是，先生产一个含空字符串的数组res[""]，然后便利S，每次将res中的每个元素后增加一个字母，再添加到res后面，最终set一下除去所有重复元素，

很遗憾，time花费过长。

这里的答案是，先生产一个含有26个0元素的数组end，便利S，将遇到的字母转换成0 — 26 的数字，然后每次更新对应的end数组位置的值，每次变为sum(end)+1，每次改变的大小与我的思路一样，

但复杂度降低了很多。