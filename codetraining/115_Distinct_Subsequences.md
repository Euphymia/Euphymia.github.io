#115_Distinct_Subsequences

------

> - 问题
> - 代码
> - 思路

------

## 问题

 115.不同的子序列

 

给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

 

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

 

示例 1:

 

输入: S = "rabbbit", T = "rabbit"

输出: 3

解释:

 

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。

(上箭头符号 ^ 表示选取的字母)

 

rabbbit

^^^^ ^^

rabbbit

^^ ^^^^

rabbbit

^^^ ^^^

示例 2:

 

输入: S = "babgbag", T = "bag"

输出: 5

解释:

 

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 

(上箭头符号 ^ 表示选取的字母)

 

babgbag

^^ ^

babgbag

^^    ^

babgbag

^    ^^

babgbag

  ^  ^^

babgbag

​    ^^^

## 代码

```python
import collections
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sub_s=collections.OrderedDict({"":1})
        for i in s:
            temp=reversed([i for i in sub_s.keys()])
            for j in temp:
                new_s=j+i
                if t.startswith(new_s):
                    sub_s[new_s]=sub_s.get(new_s,0)+sub_s[j]
        return sub_s.get(t,0)
if __name__ == "__main__":
    sl=Solution()
    S = "rabbbit"
    # S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    # T = "bddabdcae"
    T = "rabbit"
    print(sl.numDistinct(S,T))
```

## 思路

思路：

很有意思，这次我用字典来保存需要的子序列，因为使用数组会tle，其他的就是寻找子序列的很常见的方法。