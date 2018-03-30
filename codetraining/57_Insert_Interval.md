#57 Insert Interval

---

> * 问题
> * 代码
> * 主要思路

---

## 问题

问题：

给出一个无重叠的按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1 : 给定区间[1, 3],[ 6, 9 ] ，插入并合并[2, 5] 得到[1, 5],[ 6, 9 ].

示例 2 : 给定区间[1, 2],[ 3, 5 ],[ 6, 7 ]，[ 8, 10 ],[ 12, 16 ] ，插入并合并[4, 9] 得到[1, 2],[ 3, 10 ],[ 12, 16 ].

这是因为新的区间[4, 9] 与[3, 5],[ 6, 7 ],[ 8, 10 ] 重叠。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
// Definition for an interval.
// 定义区间结构体
struct Interval {
     int start;
     int end;
     Interval() : start(0), end(0) {}
     Interval(int s, int e) : start(s), end(e) {}
};
class Solution
{
  public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval)
    {
        vector<Interval> res;
        if (intervals.empty())
        {
            res.push_back(newInterval);
            return res;
        }
        int cur = 0;
        while (cur < intervals.size() & intervals[cur].end < newInterval.start)
        {
            res.push_back(intervals[cur++]);
        }
        while (cur < intervals.size() & intervals[cur].start <= newInterval.end)
        {
            newInterval.start = min(newInterval.start, intervals[cur].start);
            newInterval.end = max(newInterval.end, intervals[cur].end);
            cur++;
        }
        res.push_back(newInterval);
        while (cur < intervals.size())
        {
            res.push_back(intervals[cur++]);
        }
        return res;
    }
};
int main(){
    Solution sl;
    Interval i0(1,2),i1(3,5),i2(6,7),i3(8,10),i4(12,16);
    vector<Interval> res,intervals={i0,i1,i2,i3,i4};
    Interval inserter(4,9);
    res=sl.insert(intervals,inserter);
    for(int i=0;i<res.size();i++){
        cout<<res[i].start<<","<<res[i].end<<endl;
    }
    getchar();
    return 0;
}
```

## 主要思路

![Insert Interval.png](/InsertInterval.png)

如上图所示，整个过程分为三个while子句。