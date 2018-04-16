#69 Sqrt(x)

---

> * 问题
> * 代码
> * 思路

---

## 问题

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4

Output: 2

Example 2:

Input: 8

Output: 2

Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    int mySqrt(int x)
    {
        int low=0,high=x,mid;
        if(x<2) return x;
        while(low<high){
            mid=(low+high)/2;
            if(x/mid>=mid) low=mid+1;
            else high=mid;
        }
        return high-1;
    }
};
int main(){
    Solution sl;
    cout<<sl.mySqrt(8);
    getchar();
    return 0;
}
```

## 思路 

选一个候选值的平方，然后和x比较大小，为了缩短查找时间，我们采用二分搜索法来找平方根

找最后一个不小于目标值的数