#2018 网易机试题--相反数

---

> * 问题
> * 代码

---

## 问题

相反数

为了得到一个数的”相反数”, 我们将这个数的数字顺序颠倒, 然后再加上原先的数得到”相反数”。例如, 

为了得到1325的”相反数”, 首先我们将该数的数字顺序颠倒, 我们得到5231, 之后再加上原先的数,

 我们得到5231 + 1325 = 6556.如果颠倒之后的数字有前缀零, 前缀零将会被忽略。例如n = 100, 颠倒之后是1.输入描述 : 

 输入包括一个整数n, (1 ≤ n ≤ 10 ^ 5)

输出描述 : 输出一个整数,

表示n的相反数

输入例子1 : 1325

输出例子1 : 6556

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
int main(){
    int num=0,renum=0,res=0,temp=0;
    cin>>res;
    num=res;
    getchar();
    while(num){
        temp=num%10;
        num=num/10;
        renum=renum*10+temp;
    }
    cout<<renum+res<<endl;
    getchar();
    return 0;
}
```

```python
#python
num=input()
num1=int(num[::-1])
num2=int(num)

print(num1+num2)
```

