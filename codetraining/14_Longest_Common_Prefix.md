#14 Longest Common Prefix

---

> * 问题
> * 代码
> * 思路

---

## 问题

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]

输出: "fl"

示例 2:

输入: ["dog","racecar","car"]

输出: ""

解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res="";
        if(strs.empty()) return res;
        if(strs.size()==1) return strs[0];
        int len=strs[0].size();
        for(int i=1;i<strs.size();++i){
            len=strs[i].size()>len? len:strs[i].size(); 
        }
        for(int i=0;i<len;++i){
            int j=0;
            for(;j<strs.size()-1;){
                if(strs[j][i]==strs[j+1][i]) ++j;
                else return res;
            }
            if(j==strs.size()-1) res+=strs[0][i];
        }
        return res;
    }
};
int main()
{
    Solution sl;
    vector<string> v = {"flower", "flow", "flight"};
    cout<<sl.longestCommonPrefix(v);
    getchar();
    return 0;
}
```

## 思路

先找出最短单词的长度，接下里用两个for循环找出最长前缀