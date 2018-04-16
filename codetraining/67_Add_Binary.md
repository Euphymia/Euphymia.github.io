#67 Add Binary

---

> * 问题
> * 代码
> *  ? :运算符的用法

---

## 问题

二进制求和。 

给定两个二进制字符串，返回他们的和（用二进制表示）。

案例：

a = "11" b = "1" 返回 "100" 。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    string addBinary(string a, string b)
    {
        char carry='0';
        string res="";
        int i=a.length()-1,j=b.length()-1;
        for(;i>=0&&j>=0;){
            char ch=a[i]-'0'+b[j]-'0'+carry;
            if(ch>='2'){
                carry = '1';
                ch=ch-2;
            }
            else{
                carry = '0';
            }
            res=ch+res;
            i--;
            j--;
        }
        if(i>=0)
            for(;i>=0;i--){
                char ch=a[i]-'0'+carry;
                if(ch=='2'){
                    carry = '1';
                    ch='0';
                }
                else carry='0';
                res=ch+res;
            }   
        else
            for(;j>=0;j--){
                char ch=b[j]-'0'+carry;
                if(ch=='2'){
                    carry = '1';
                    ch='0';
                }
                else carry = '0';
                res=ch+res;
            }   
        
        return carry=='1'? '1'+res:res;
    }
};
int main()
{
    Solution sl;
    cout<<sl.addBinary("1111","1111");
    getchar();
    return 0;
}
```

## ? :运算符的用法

在某些情况下，可以用条件运算符“ ?: ”来简化if语句。 基本格式

“?: ”是一个三元运算符，其构成的表达式格式为：<表达式1> ? <表达式2> : <表达式3> 

例如： 

```c++

if (a > b) max = a;

else max = b;

可写成：

max = a > b ? a : b;

或者

return a>b? a:b;
```