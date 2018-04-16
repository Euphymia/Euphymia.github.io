#49 Group Anagrams

---

> * 问题
> * 代码
> * 思路
> * auto的用法
> * for循环的五种语法

---

## 问题

群组错位词

错位词就是两个字符串中字母出现的次数都一样，只是位置不同，比如abc，bac, cba等它们就互为错位词

给定一个字符串数组，将相同错位词组合在一起。（错位词是指颠倒字母顺序而成的字）

例如，给定["eat", "tea", "tan", "ate", "nat", "bat"] ，返回：

[[ "ate", "eat", "tea" ],

[ "nat", "tan" ],

["bat"]]

## 代码

```c++
#include <bits/stdc++.h>
    using namespace std;
class Solution
{
    public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> res;
        unordered_map<string,vector<string>> m;
        for(auto str : strs){
            string t = str;
            sort(t.begin(),t.end());
            m[t].push_back(str);
        }
        for(auto a : m){
            res.push_back(a.second);
        }
        return res;
    }
};
int main()
{
    Solution sl;
    vector<string> v1 = {"eat", "tea", "tan", "ate", "nat", "bat" };
    vector<vector<string>> res;
    res=sl.groupAnagrams(v1);
    for(auto i : res){
        for(auto j : i){
            cout<<j<<",";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

把错位词的字符顺序重新排列，那么会得到相同的结果，所以重新排序是判断是否互为错位词的方法，

由于错位词重新排序后都会得到相同的字符串，我们以此作为key，将所有错位词都保存到字符串数组中，

建立key和字符串数组之间的映射，最后再存入结果res中即可。

## auto的用法

C++ 11 auto

auto可以在声明变量的时候根据变量初始值的类型自动为此变量选择匹配的类型，类似的关键字还有decltype。举个例子：

```c++
int a = 10;

auto au_a = a; //自动类型推断，au_a为int类型

cout << typeid(au_a).name() << endl;

typeid运算符可以输出变量的类型。程序的运行结果输出了

>>>int
```

## for循环的五种用法

```c++
#include <algorithm>
#include <vector>
    //////////////////////////////////////////////
    int nArray[] = {0, 1, 2, 3, 4, 5};
std::vector<int> vecNum(nArray, nArray + 6);
CString strText;
// 第一种用法：最原始的语法(用下标)
for (size_t i = 0; i < vecNum.size(); ++i)
{
    strText.Format("%d", nArray[i]);
    AfxMessageBox(strText);
}

// 第二种用法：最原始的语法(用迭代器)
for (auto it = vecNum.begin(); it != vecNum.end(); ++it)
{
    strText.Format("%d", *it);
    AfxMessageBox(strText);
}

// 第三种用法：简化数组遍历语法(从vs2008开始支持)
for
    each(auto item in vecNum)
    {
        strText.Format("%d", item);
        AfxMessageBox(strText);
    }

// 第四种用法：STL函数
std::for_each(vecNum.begin(), vecNum.end(), [](int item) {
    CString strText;
    strText.Format("%d", item);
    AfxMessageBox(strText);
});

// 第五种用法：C++11新增加的(VS2012支持)
for (auto item : vecNum)
{
    strText.Format("%d", item);
    AfxMessageBox(strText);
}
```

