#78 Subsets

---

> * 问题
> * 代码
> * 思路

---

## 问题

子集合

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,

If nums = [1,2,3], a solution is:

[

  [3],

  [1],

  [2],

  [1,2,3],

  [1,3],

  [2,3],

  [1,2],

  []

]

## 代码

```C++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res(1);
        for(int i=0;i<nums.size();i++){
            int size=res.size();
            for(int j=0;j<size;j++){
            res.push_back(res[j]);
            res[j].push_back(nums[i]);
            }
        }
        return res;
    }
};
int main()
{
    Solution sl;
    vector<int> nums={1,2,3};
    auto res=sl.subsets(nums);
    for(int i=0;i<res.size();i++){
        for(int j=0;j<res[i].size();j++){
            cout<<res[i][j]<<",";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

最开始是空集，那么我们现在要处理1，就在空集上加1，为[1] ，现在我们有两个自己[] 和[1] ，

下面我们来处理2，我们在之前的子集基础上，每个都加个2，可以分别得到[2] ，[1, 2] ，

那么现在所有的子集合为[], [1], [2], [ 1, 2 ] ，同理处理3的情况可得[3], [ 1, 3 ], [ 2, 3 ], [ 1, 2, 3 ]