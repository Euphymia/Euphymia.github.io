#46 Permutations

---

> * 问题
> * 代码
> * 思路

---

## 问题

全排列。 给定一个含有不同数字的集合，返回所有可能的全排列。

比如，

[1, 2, 3] 具有如下排列：

[[ 1, 2, 3 ],

[ 1, 3, 2 ],

[ 2, 1, 3 ],

[ 2, 3, 1 ],

[ 3, 1, 2 ],

[ 3, 2, 1 ]]

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> res;
        permuteRecursive(nums,0,res);
        return res;
    }
    void permuteRecursive(vector<int> &nums,int start,vector<vector<int>> &res){
      if(start == nums.size()){
        res.push_back(nums);
        return;
      }
      for(int i=start;i<nums.size();++i){
        swap(nums[start],nums[i]);
        permuteRecursive(nums,start+1,res);
        swap(nums[start],nums[i]);
      }
    }
};
int main(){
  Solution sl;
  vector<int> v1={1,2,3,4};
  vector<vector<int>> res;
  res=sl.permute(v1);
  cout<<res.size()<<endl;
  for(int i=0;i<res.size();++i){
    for(int j=0;j<res[i].size();++j){
      cout<<res[i][j];
    }
    cout<<endl;
  }
  getchar(); 
  return 0;
}
```

## 思路

通过递归不停的交换nums数组的元素，知道全部交换过为止。