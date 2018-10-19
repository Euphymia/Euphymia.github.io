#906_Super_Palindromes

------

> - 问题
> - 代码
> - 思路

## 问题

\906. Super Palindromes

如果它是回文，它的平方根也是回文即称这个正整数是一个  superpalindrome，  。

现在，给定两个正整数L和R（表示为字符串），返回包含范围内的superpalindromes的数量[L, R]。

例1：

输入： L = “4”，R = “1000”

输出： 4

 说明： 4, 9, 121和484是superpalindromes。

请注意，676不是superpalindrome：26 * 26 = 676，但26不是回文。

注意： 

1 <= len(L) <= 18

1 <= len(R) <= 18

L并且R是表示范围内的整数的字符串[1, 10 ^ 18)。

int(L) <= int(R)

## 代码

```python
import math
class Solution(object):
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        left = int(math.floor(math.sqrt(L)))
        right = int(math.ceil(math.sqrt(R)))
        n1, n2 = len(str(left)), len(str(right))
        n1 = n1//2 if n1 % 2 == 0 else n1//2+1
        n2 = n2//2 if n2 % 2 == 0 else n2//2+1
        start = int('1' + '0'*(n1-1))
        end = int('9'*n2)+1
        ans = 0
        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])
            num2 = int(x + x[:-1][::-1])
            for num in [num1, num2]:
                cand = num*num
                if cand >= L and cand <= R and str(cand) == str(cand)[::-1]:
                    ans += 1
        return ans


if __name__ == "__main__":
    sl = Solution()
    L="4"
    R="1000000"
    print(sl.superpalindromesInRange(L,R))
```

## 思路

思路，一个个试是不可能的，时间复杂度太高。

首先取L，R的平方根，再将平方根取长度的一半(用于回文串的拼接)，找到一个大致的长度范围

​    start = int('1' + '0'*(n1-1))

​    end = int('9'*n2)+1

然后在将这里的数开始拼接成回文串，一共有两种拼法，直接逆序拼接，第二种删除最后一个数，再逆序拼接。

最后判断这个数的平方，如果在L，R中，则加入到ans中即可。