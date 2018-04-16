#77 Combinations

---

> * 问题
> * 代码
> * 思路

---

## 问题

组合项。

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,

If n = 4 and k = 2, a solution is:

[

  [2,4],

  [3,4],

  [2,3], 

  [1,2],

  [1,3],

  [1,4],

]

## 代码

```C++
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> out;    
        helper(n,k,1,res,out);
        return res;
    }
    void helper(int n,int k,int level,vector<vector<int>>& res,vector<int>& out){
        if(out.size()==k) {
            res.push_back(out);
        }
        for(int i=level;i<=n;i++){
            out.push_back(i);
            helper(n,k,i+1,res,out);
            out.pop_back();
        }
    }
};
int main(){
    Solution sl;
    vector<vector<int>> res;
    res=sl.combine(5,3);
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

这道题让求1到n共n个数字里k个数的组合数的所有情况，还是要用深度优先搜索DFS来解，根据以往的经验，

像这种要求出所有结果的集合，一般都是用DFS调用递归来解。那么我们建立一个保存最终结果的大集合res，

还要定义一个保存每一个组合的小集合out，每次放一个数到out里，如果out里数个数到了k个，则把out保存到最终结果中，否则在下一层中继续调用递归。