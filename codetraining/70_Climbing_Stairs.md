#70 Climbing Stairs

---

> * 问题
> * 代码
> * 主要思路

---

## 问题

你在爬一个楼梯。到达顶部有n级阶梯。

每次你可以选择爬一级或者二级。在多少不同的方式去到达顶部？

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;

class Solution
{
  public:
    int climbStairs(int n)
    {
        if (n == 1 || n == 2)
        {
            return n;
        }
        else
        {
            return climbStairs(n - 2) + climbStairs(n - 1);
        }
    }
    int climbStairs2(int n)
    {
        if (n == 1 || n == 2)
        {
            return n;
        }
        int n1 = 1;
        int n2 = 2;
        for (int i = 3; i <= n; i++)
        {
            int temp = n1 + n2;
            n1 = n2;
            n2 = temp;
        }
        return n2;
    }
};
int main(){
    Solution sl;
    cout<<sl.climbStairs(6)<<endl;
    cout<<sl.climbStairs2(6);
    getchar();
    return 0;
}
```

## 主要思路

分析：

当n = 1，无疑只有一种方式，s = 1。 n = 2，s = 2。 n = 3，s = 3。 n = 4，s = 5。 

我们发现这个实际是一个斐波那契数列。第一反应是递归实现，f(n) = f(n - 1) + f(n - 2) ，

但是递归实现，有多次重复计算，比如在计算f(n - 1) 时，需要使用f(n - 2) + f(n - 3) ，

但是这个时候另一个递归调用已经去算了f(n - 2) ，相当于f(n - 2) 被计算了2次，这种重复计算的情况普遍存在，

将会浪费大量计算时间。很自然的想到反过来操作，递归是从目标算到基础值，而我们可以采用迭代从基础值1, 2累加上去。