#12 Integer to Roman

---

> * 问题
> * 代码
> * 思路

---

## 问题

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

例如：输入 1

输出 I

##代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    string intToRoman(int num)
    {
        vector<string> M = {"", "M", "MM", "MMM"};
        vector<string> C = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        vector<string> X = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        vector<string> I = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }
};
int main()
{
    Solution sl;
    int num=3499;
    string str;
    str=sl.intToRoman(num);
    cout<<str;
    cin.get();
    return 0;
}
```

