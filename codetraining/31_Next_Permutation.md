#31 Next Permutation

---

> * 问题
> * 代码
> * 思路

---

## 问题

下一个排列

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len=nums.size()-1;
        for(int i=len;i>0;i--){
            if(nums[i-1]<nums[i]){
                for(int j=len;j>i-1;j--){
                    if(nums[j]>nums[i-1]){
                        swap(nums[j],nums[i-1]);
                        reverse(nums.begin()+i,nums.end());
                        return;
                    }
                }
            }
        }
        reverse(nums.begin(), nums.end());
    }
};
int main(){
    Solution sl;
    vector<int> nums={1,2,7,4,3,1};
    sl.nextPermutation(nums);
    for(int i=0;i<nums.size();i++){
        cout<<nums[i]<<","<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，

然后我们再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可