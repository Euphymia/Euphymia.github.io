#56 Merge Intervals

---

> * 问题
> * 代码
> * sort()函数
> * max()函数

---

## 问题

问题：

给出一个区间的集合, 请合并所有重叠的区间。

示例： 给出[1, 3],[ 2, 6 ], [ 8, 10 ], [ 15, 18 ],

返回[1, 6], [ 8, 10 ], [ 15, 18 ].

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
// Definition for an interval.
struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
class Solution
{
    public:
    vector<Interval> merge(vector<Interval> &ins)
    {
        if (ins.empty())
            return vector<Interval>{};
        vector<Interval> res;
        sort(ins.begin(), ins.end(), [](Interval a, Interval b) { return a.start < b.start; });
        res.push_back(ins[0]);
        for (int i = 1; i < ins.size(); i++)
        {
            if (res.back().end < ins[i].start)
                res.push_back(ins[i]);
            else
                res.back().end = max(res.back().end, ins[i].end);
        }
        return res;
    }
};
int main()
{
    Solution sl1;
    Interval i0(1, 3), i1(2, 6), i2(8, 10), i3(15, 18);
    vector<Interval> intervals = {i0, i1, i2, i3};
    intervals=sl1.merge(intervals);
    for(int i=0;i<intervals.size();i++){
        cout<<intervals[i].start<<","<<intervals[i].end<<endl;
    }
    getchar();
    return 0;
}
```

## sort()函数

sort() 函数的使用方法：

Sort函数有三个参数：

（1）第一个是要排序的数组的起始地址。 

（2）第二个是结束的地址（最后一位要排序的地址）

（3）第三个参数是排序的方法，可以是从大到小也可是从小到大，还可以不写第三个参数，此时默认的排序方法是从小到大排序。 

sort() 可以通过重写complare方法自定义比较方法。

例如

// complare方法定义在main函数之前。

bool complare(int a, int b)

{

​    // 从大到小排序

​    return a > b;

}

int a[10] = {9, 6, 3, 8, 5, 2, 7, 4, 1, 0};

sort(a, a + 10, complare); //在这里就不需要

## max()函数

max()函数的使用方法：

int a=0;

a=max(3,8);

cout<<a;   // a=8