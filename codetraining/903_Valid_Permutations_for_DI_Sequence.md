#Valid_Permutations_for_DI_Sequence

------

> - 问题
> - 代码
> - 思路

## 问题

903. DI 序列的有效排列

我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）

有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：

 

如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；

如果 S[i] == 'I'，那么 P[i] < P[i+1]。

有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10 ^ 9 + 7.

示例：

输入："DID"

输出：5

解释：

(0, 1, 2, 3) 的五个有效排列是：

(1, 0, 3, 2)

(2, 0, 3, 1)

(2, 1, 3, 0)

(3, 0, 2, 1)

(3, 1, 2, 0)

提示：

 

1 <= S.length <= 200

S 仅由集合 {'D', 'I'} 中的字符组成。

## 代码

```python
class Solution:

    def numPermsDISequence(self, S):
            dp = [1] * (len(S) + 1)
            for c in S:
                if c == "I":
                    dp = dp[:-1]
                    for i in range(1, len(dp)):
                        dp[i] += dp[i - 1]
                else:
                    dp = dp[1:]
                    for i in range(len(dp) - 1)[::-1]:
                        dp[i] += dp[i + 1]
            return dp[0] % (10**9 + 7)
if __name__=="__main__":
    sl=Solution()
    print(sl.numPermsDISequence("DID"))
```

## 思路

思路：

![903_Valid_Permutations_for_DI_Sequence](/903_Valid_Permutations_for_DI_Sequence.png)

通过这个图我们可以看出来一定的规律

即当遇到'D'时，将数组[1,1,1,1]中除了最后一个数，所有的数向后加。

遇到'I'时，将数组中所有的数除了第一个，向前加。