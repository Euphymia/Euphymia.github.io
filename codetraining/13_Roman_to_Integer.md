# 13 Roman to Integer

---

> * 问题
> * 代码
> * 思路

---

## 问题

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

例如：输入 II

输出 2

## 代码

```c++
#include <bits/stdc++.h>
    using namespace std;
class Solution
{
    public:
    int romanToInt(string s)
    {
        int res=0;
        for(int i=s.length()-1;i>=0;i--){
            char ch=s[i];
            switch(ch){
                case 'I':
                res+=(res>=5? -1:1);
                break;
                case 'V':
                res+=5;
                break;
                case 'X':
                res+=(res>=50? -10:10);
                break;
                case 'L':
                res+=50;
                break;
                case 'C':
                res+=(res>=500? -100:100);
                break;
                case 'D':
                res+=500;
                break;
                case 'M':
                res+=1000;
                break;
            }
        }
        return res;   
    }
};
int main()
{
    Solution sl;
    string str="MIV";
    cout<<sl.romanToInt(str);
    cin.get();
    return 0;
}
```

## 思路

罗马数转化成数字问题，我们需要对于罗马数字很熟悉才能完成转换。以下截自百度百科：

罗马数字是最早的数字表示方式，比阿拉伯数字早2000多年，起源于罗马。 如今我们最常见的罗马数字就是钟表的表盘符号：

Ⅰ，Ⅱ，Ⅲ，Ⅳ（IIII），Ⅴ，Ⅵ，Ⅶ，Ⅷ，Ⅸ，Ⅹ，Ⅺ，Ⅻ…… 对应阿拉伯数字（就是现在国际通用的数字），

就是1，2，3，4，5，6，7，8，9，10，11，12。（注：阿拉伯数字其实是古代印度人发明的，后来由阿拉伯人传入欧洲，

被欧洲人误称为阿拉伯数字。）

基本字符

I 1

V 5

X 10

L 50

C 100

D 500

M 1000