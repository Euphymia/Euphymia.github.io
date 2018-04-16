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
using namespace std;
class Solution {
public:
    int numDecodings(string s) {
        int len=s.size();
        if(len==0||s[0]=='0') return 0;
        if(len==1) return 1;
        int fn_1=1,fn_2=1,res=0;
        for(int i=1;i<len;++i){
            int temp=fn_1;
            if(isValid(s[i])&&isValid(s[i-1],s[i])) res=fn_1+fn_2;
            if(!isValid(s[i])&&isValid(s[i-1],s[i])) res=fn_2; 
            if(isValid(s[i])&&!isValid(s[i-1],s[i])) res=fn_1;
            if(!isValid(s[i])&&!isValid(s[i-1],s[i])) return 0;
            fn_1=res;
            fn_2=temp;
        }
        return res;
    }
    bool isValid(char a){
        if(a=='0') return false;
        return true;
    }
    bool isValid(char a,char b){
        if(a=='1'||(a=='2'&&b<='6')) return true;
        return false;
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