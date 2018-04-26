#29 Divide Two Integers

---

> * 问题
> * 代码
> * 思路
> * C\C++ 中的绝对值函数

---

## 问题

两数相除：

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3

输出: 3

示例 2:

输入: dividend = 7, divisor = -3

输出: -2

说明:

被除数和除数均为 32 位有符号整数。

除数不为 0。

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2e31,  2e31 − 1]。本题中，如果除法结果溢出，则返回 2e31 − 1。

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(divisor==0||(dividend==INT_MIN&&divisor==-1)) return INT_MAX;
        int sign=(divisor>0)^(dividend>0)? -1:1;
        long long did=labs(dividend),dis=labs(divisor);
        int res=0;
        while(did>=dis){
            long long temp=dis,multi=1;
            // 通过位运算，向左移以为表示数字*2，从而化简运算过程。
            while(did>(temp<<1)){
                temp=temp<<1;
                multi=multi<<1;
            }
            did-=temp;
            res+=multi;
        }
        return sign==1? res:-res;
    }
};
int main(){
    Solution sl;
    cout<<sl.divide(-10,3);
    getchar();
    return 0;
}
```

## 思路

如果被除数大于或等于除数，则进行如下循环，定义变量t等于除数，定义计数p，当t的两倍小于等于被除数时，进行如下循环，t扩大一倍，p扩大一倍，然后更新res和m。这道题的OJ给的一些test case非常的讨厌，因为输入的都是int型，比如被除数是-2147483648，在int范围内，当除数是-1时，结果就超出了int范围，需要返回INT_MAX，所以对于这种情况我们就在开始用if判定，将其和除数为0的情况放一起判定，返回INT_MAX。然后我们还要根据被除数和除数的正负来确定返回值的正负，这里我们采用长整型long来完成所有的计算，最后返回值乘以符号即可

## C\C++ 中的绝对值函数

abs()、cabs()、fabs()、labs()

不同类型的数据使用不同类型的绝对值函数：

整型：

int abs(int i)  //返回整型参数i的绝对值 

复数：

double cabs(struct complex znum)  //返回复数znum的绝对值  

双精度浮点型：

double fabs(double x)  //返回双精度参数x的绝对值    

长整型：

long labs(long n)  //返回长整型参数n的绝对值 