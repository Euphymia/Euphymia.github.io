#30_Substring with Concatenation of All Words

---

> * 问题
> * 代码
> * 思路
> * set和multiset的使用方法

---

## 问题

给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:

  s = "barfoothefoobarman",

  words = ["foo","bar"]

输出: [0,9]

解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。

输出的顺序不重要, [9,0] 也是有效答案。

示例 2:

输入:

  s = "wordgoodstudentgoodword",

  words = ["word","student"]

输出: []

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        if (words.size() == 0 || s.size() == 0 ||words[0].size() > s.size()||s.size()<(words[0].size()*words.size()))
            return res;
        int len=words[0].size();
        // unordered_map<string,int> map;
        multiset<string> mset;
        for(int i=0;i<words.size();++i){
            // if(map.find(words[i])!=map.end()) map[words[i]]+=1;
            // else map[words[i]]=1;
            mset.insert(words[i]);
        }
        for(int i=0;i<=s.size()-len;++i){
            // unordered_map<string,int> temp=map;
            multiset<string> temp=mset;
            int j=i;
            while (temp.find(s.substr(j, len)) != temp.end()){
                // if(temp[s.substr(j,len)]==1) temp.erase(s.substr(j, len));
                // else temp[s.substr(j, len)]-=1;
                multiset<string>::iterator it = temp.find(s.substr(j, len));
                if (it != temp.end()) {
                    temp.erase(it);  //这里是删除其中的一个x;  删除的是一个位置  而erase是删除所有位置
                }
                j += len;
            }
            if(temp.empty()) res.push_back(i);
        }
        return res;
    }
};
int main()
{
    Solution sl;
    string s = "a";
    vector<string> words = {"a"};
    vector<int> res;
    res=sl.findSubstring(s,words);
    for(int i=0;i<res.size();i++){
        cout<<res[i]<<endl;
    }
    getchar();
    return 0;
}
```

## 思路

先将words中的元素保存到以个multiset结构体中(因为words中元素可能重复),然后将s从第一个字符开始，每取words中单词的长度与multiset中的元素比较，发现在set中则删除set中相应的元素并继续比较，若set删空，则说明匹配到一个目标子串，退出并从下一个字符开始重新比较。

##set和multiset的使用方法

C++ STL set和multiset的使用

std::set<int> s;那个s这个对象里面存贮的元素是从小到大排序的，(因为用std::less作为比较工具。)

1，set的含义是集合，它是一个有序的容器，里面的元素都是排序好的，支持插入，删除，查找等操作，就   像一个集合一样。所有的操作的都是严格在logn时间之内完成，效率非常高。 set和multiset的区别是：set插入的元素不能相同，但是multiset可以相同。

   创建 multiset<ss> base;

   删除：如果删除元素a,那么在定义的比较关系下和a相等的所有元素都会被删除

   想要删除某个元素需要该元素的iterator。

   base.count( a )：set能返回０或者１，multiset是有多少个返回多少个．

   Set和multiset都是引用<set>头文件,复杂度都是logn

2，Set中的元素可以是任意类型的，但是由于需要排序，所以元素必须有一个序，即大小的比较关系，比如   整数可以用＜比较．

3，自定义比较函数；

​    include<set>

​    typedef struct

​    { 定义类型　}

​    ss(类型名);

​    struct cmp

​    {

​          bool operator()( const int &a, const int &b ) const

​             { 定义比较关系＜}

​    };

​    (运算符重载，重载<)

​    set<ss> base; ( 创建一个元素类型是ss,名字是base的set )

​    注：定义了＜，＝＝和＞以及＞＝，＜＝就都确定了，STL的比较关系都是用＜来确定的，所以必须通    过定义＜　－－“严格弱小于”来确定比较关

4，set的基本操作：

begin()         返回指向第一个元素的迭代器

clear()         清除所有元素

count()         返回某个值元素的个数

empty()         如果集合为空，返回true

end()           返回指向最后一个元素的迭代器

equal_range()   返回集合中与给定值相等的上下限的两个迭代器

erase()         删除集合中的元素

find()          返回一个指向被查找到元素的迭代器

get_allocator() 返回集合的分配器

insert()        在集合中插入元素

lower_bound()   返回指向大于（或等于）某值的第一个元素的迭代器

key_comp()      返回一个用于元素间值比较的函数

max_size()      返回集合能容纳的元素的最大限值

rbegin()        返回指向集合中最后一个元素的反向迭代器

rend()          返回指向集合中第一个元素的反向迭代器

size()          集合中元素的数目

swap()          交换两个集合变量

upper_bound()   返回大于某个值元素的迭代器

value_comp()    返回一个用于比较元素间的值的函数