# Three Sum

---

> * 问题
> * 代码
> * 具体方法

---

## 问题

[LeetCode] 3Sum 三数之和

Given an array S of n integers,are there elements a, b, c in S such that a + b + c = 0 ? 

Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet(a, b, c) must be in non - descending order.(ie, a ≤ b ≤ c)The solution set must not contain  duplicate triplets.For example,

given array S = {-1 0 1 2 - 1 - 4},

A solution set is : (-1, 0, 1)(-1, -1, 2) 

## 代码

```c++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
  public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        // res 用来存放结果三元组
        vector<vector<int>> res;
        // 先使用sort()排序
        sort(nums.begin(), nums.end());
        // 将求三数和转换为求两数和，从第一个元素开始，确定一个元素，寻找剩下和为target的两个元素。
        for (int k = 0; k < nums.size(); ++k)
        {
            // nums是从小到大顺序排列的，如果最小的大于0.则不可能存在三数和等于0的三元组
            if (nums[k] > 0)
                break;
            // 跳过重复元素
            if (k > 0 && nums[k] == nums[k - 1])
                continue;
            int target = 0 - nums[k];
            int i = k + 1, j = nums.size() - 1;
            // 在剩下的元素里找和为target的元素。
            while (i < j)
            {
                if (nums[i] + nums[j] == target)
                {
                    res.push_back({nums[k], nums[i], nums[j]});
                    while (i < j && nums[i] == nums[i + 1])
                        ++i;
                    while (i < j && nums[j] == nums[j - 1])
                        --j;
                    ++i;
                    --j;
                }
                else if (nums[i] + nums[j] < target)
                    ++i;
                else
                    --j;
            }
        }
        return res;
    }
};
int main(){
    vector<int> nums={-1,1,0,2,-1,4};
    vector<vector<int>> res;
    Solution sl;
    res=sl.threeSum(nums);
    for(int i=0;i<res.size();i++){
        for(int j=0;j<3;j++){
            cout<<res[i][j]<<" ";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

## 具体方法

sort排序方法

c++ 标准库里的排序函数的使用方法

I）Sort函数包含在头文件为 #include<algorithm>

的c++ 标准库中，调用标准库里的排序方法可以不必知道其内部是如何实现的，只要出现我们想要的结果即可！

II）Sort函数有三个参数：

（1）第一个是要排序的数组的起始地址。 （2）第二个是结束的地址（最后一位要排序的地址）

（3）第三个参数是排序的方法，可以是从大到小也可是从小到大，还可以不写第三个参数，此时默认的排序方法是从小到大排序。 

​    Sort函数使用模板 : Sort(start, end, , 排序方法)

​    升序：sort(begin, end, less<data - type>());

​    降序：sort(begin, end, greater<data - type>());