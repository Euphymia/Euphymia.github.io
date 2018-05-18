#46 Permutations

---

> * 问题
> * 代码
> * 思路
> * python列表交换两个元素
> * python.append() 方法覆盖前面元素解决方法

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

```python
import copy
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.permuteRecursive(nums,0,res)
        return res
    def permuteRecursive(self,nums,start,res):
        if start==len(nums):
            temp=copy.deepcopy(nums)
            res.append(temp)
            return
        else:
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                self.permuteRecursive(nums,start+1,res)
                nums[start],nums[i]=nums[i],nums[start]
sl=Solution()
nums=[1,2,3]
res=[]
res=sl.permute(nums)
print(res)
```



## 思路

通过递归不停的交换nums数组的元素，知道全部交换过为止。

## python列表交换两个元素

python列表交换两个元素：

nums[a], nums[b] = nums[b], nums[a]

##python.append() 方法覆盖前面元素解决方法

先进行深拷贝

import copy

copy.deepcopy(a)

再将a append到列表中即可