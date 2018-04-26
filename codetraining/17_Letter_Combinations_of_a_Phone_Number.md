#17 Letter Combinations of a Phone Number

---

> * 问题
> * 代码
> * 思路

---

## 问题

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射与电话按键相同。注意 1 不对应任何字母。

输入："23"

输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.size()==0) return res;
        string letter="";
        conbination(digits,res,0,letter);
        return res;
    }
    void conbination(string digits,vector<string>& res,int start,string letter){
        if(start==digits.size()){
            res.push_back(letter);
            return ;
        }
        vector<string> dic={"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        int num=digits[start]-50;
        for (int i = 0; i < dic[num].size(); i++){
            letter += dic[num][i];
            conbination(digits, res, start + 1, letter);
            letter = letter.substr(0, letter.size() - 1);
        }
        return ;
    }
};
int main(){
    Solution sl;
    vector<string> res;
    res=sl.letterCombinations("28");
    for(int i=0;i<res.size();i++){
        cout<<res[i]<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

使用递归的思想便利所有的情况。

重点：在循环中，先添加一个字符，进入下一次递归，删除上次添加的字符，进入迭代。