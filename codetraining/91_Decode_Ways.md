#91 Decode Ways

---

> * 问题
> * 代码
> * 思路

---

## 问题

包含 A-Z 的字母的消息通过以下规则编码：

'A' -> 1

'B' -> 2

...

'Z' -> 26

给定一个包含数字的编码消息，请确定解码方法的总数。

例如，

给定消息为 "12"， 它可以解码为 "AB"（1 2）或 "L"（12）。

"12" 的解码方法为 2 种。

## 代码

```C++
#include <bits/stdc++.h>
class Solution {
public:
    int numDecodings(string s) {
        int n=s.size();
        if(!n)  return 0;
        int *dp = new int[n];
        if(s[0] != '0')     dp[0] = 1;
        else    dp[0] = 0;
        for(int i = 1; i < n; i++){
            dp[i] = 0;
            if(s[i] != '0')     dp[i] += dp[i-1];
            int tmp = (s[i-1] - '0') * 10 + s[i] - '0';
            if(tmp >= 10 && tmp <= 26){
                if(i >= 2)  dp[i] += dp[i-2];
                else    dp[i]++;
            }
        }
        int res = dp[n-1];
        delete [] dp;
        return res;
    }
};
int main(){
    Solution sl;
    cout<<sl.numDecodings("100");
    getchar();
    return 0;
}
```

##思路

假设字符串无限长，例如ABXXXXXXX…,我们只关注前2位。 

\1. 当A单独解析时，可能的解析方式有numDecodings(BXXXXXXX…)种。 

\2. 当A和B组合解析时，可能的解析方式有numDecodings(XXXXXXX…)种。 

最后的结果，是上述2种情况的和。 

类似于爬楼梯