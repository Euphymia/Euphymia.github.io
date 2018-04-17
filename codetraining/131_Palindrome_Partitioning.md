#131 Palindrome Partitioning

---

> * 问题
> * 代码
> * 思路

---

## 问题

拆分回文串

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",

Return

[

["aa","b"],

["a","a","b"]

]

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> out;
        partitionDFS(s,0,res,out);
        return res;
    }
    void partitionDFS(string s,int start,vector<vector<string>> &res,vector<string> &out){
        if(start == s.size()){
            res.push_back(out);
            return;
        }
        for(int i=start;i<s.size();++i){
            if(isPalindrome(s,start,i)){
                out.push_back(s.substr(start,i-start+1));
                partitionDFS(s,i+1,res,out);
                out.pop_back();
            } 
        }
    }
    bool isPalindrome(string s,int start,int end){
        while (start < end) {
            if (s[start] != s[end]) return false;
            ++start;
            --end;
        }
        return true;
    }
};
int main(){
    Solution sl;
    string s="aab";
    auto res=sl.partition(s);
    // cout<<res.size();
    for(int i=0;i<res.size();++i){
        for(int j=0;j<res[i].size();++j){
            cout<<res[i][j]<<",";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

既然题目要求找到所有可能拆分成回文数的情况，那么肯定是所有的情况都要遍历到，对于每一个子字符串都要分别判断一次是不是回文数，那么肯定有一个判断回文数的子函数，还需要一个DFS函数用来递归，再加上原本的这个函数，总共需要三个函数来求解。