# String To Integer

---

> * 问题
> * 代码
> * 具体方法

---

## 问题

实现 atoi，将字符串转为整数。

提示：仔细考虑所有输入情况。如果你想挑战自己，请不要看下面并自己考虑所有可能的输入情况。

说明：这题解释的比较模糊（即没有指定输入格式）。你得事先汇集所有的输入情况。

atoi的要求：

这个函数需要丢弃之前的空白字符，直到找到第一个非空白字符。之后从这个字符开始，选取一个可选的正号或负号后面跟随尽可能多的数字，并将其解释为数字的值。

字符串可以在形成整数的字符后包括多余的字符，将这些字符忽略，这些字符对于函数的行为没有影响。

如果字符串中的第一个非空白的字符不是有效的整数，或者没有这样的序列存在，字符串为空或者只包含空白字符则不进行转换。

如果不能执行有效的转换，则返回 0。如果正确的值超过的可表示的范围，则返回 INT_MAX（2147483647）或 INT_MIN（ -2147483648）

## 代码

```c++
#include<iostream>
#include<string>
#include<limits.h>

using namespace std;
class Solution{
    public:
        int myAtoi(string str){
            // loc:当前扫描到的字符位置 n:字符串长度 sign：数字正负的记号
            int loc = 0, n = str.length(), sign = 1;
            // 最终扫描的结果，定义为最长的long
            long result = 0l;
            // 记录当前数字的长度
            int numlength = 1;
            if (str.empty())
            {
                return 0;
            }
            // if(str[loc]!=' '||str[loc]-'0'<10){
            //     return 0;
            // }
            while (loc < n && str[loc] == ' ')
                loc++;
            if (loc == str.length())
                return 0;
            if (str[loc] == '-' || str[loc] == '+')
            {
                sign = (str[loc++] == '-') ? -1 : 1;
            }
            while (loc < n && '0'<=str[loc]&& str[loc]<='9')
            {
                result = result * 10 + (str[loc++] - '0');
                numlength++;
            }
            numlength -= 1;
            if (numlength > 10)
            {
                return sign == -1 ? INT_MIN : INT_MAX;
            }
            if (numlength == 10 && result>=INT_MAX)
            {
                if (sign == 1)
                {
                    if (result < INT_MAX)
                    {
                        return result * sign;
                    }
                    else
                    {
                        return INT_MAX;
                    }
                }
                else
                {
                    if (result-1 < INT_MAX)
                        return result * sign;
                    else
                        return INT_MIN;
                }
            }
            return result * sign;
        }
};
int main(){
    Solution sl;
    cout << sl.myAtoi("-2147483647");
    getchar();
    return 0;
}
```

