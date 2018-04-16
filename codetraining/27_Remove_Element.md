#27 Remove Element

---

> * 问题
> * 代码
> * 思路

---

## 问题

移除元素(原地)

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 

with O(1) extra memory.The order of elements can be changed. It doesn't matter what you leave beyond the new length.

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    int removeElement(vector<int> &nums, int val)
    {
        int n=nums.size();
        int cnt=0;
        for(int i=0;i<n;++i){
            if(nums[i]==val) cnt++;
            else nums[i-cnt]=nums[i];
        }
        return n-cnt;
    }
};
int main()
{
    Solution sl;
    vector<int> v1={2,3,3,4,2};
    int n=sl.removeElement(v1,2);
    for(int i=0;i<n;++i){
        cout<<v1[i]<<endl;
    }

    cin.get();
    return 0;
}
```

