#3 Longest Substring Without Repeating Characters

---

> * 问题
> * 代码
> * 思路
> * unordered_map的使用方法

---

## 问题

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,

 "pwke" is a subsequence and not a substring.

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength=0,length=0;
        unordered_map<char,int> map;
        for(int i=0;i<s.size    ();++i){
            if(map.find(s[i])==map.end()){
                map[s[i]]=i;
                length+=1;
                maxLength=length>maxLength? length:maxLength;
            }
            else{
                i=map[s[i]];
                map.clear();
                length=0;
            }
        }
        return maxLength;
    }
};
int main(){
    Solution sl;
    cout << sl.lengthOfLongestSubstring("dvdf");
    getchar();
    return 0;
}
```

##思路：

创建一个unordered_map用来保存已检测到的字符。一旦出现重复则从发生重复的那个字符开始，

清空map，重新计算，并保存出现过的最大的长度。

##unordered_map的使用方法：

成员函数

=================迭代器========================= 

begin 返回指向容器起始位置的迭代器（iterator） 

end 返回指向容器末尾位置的迭代器 

cbegin 返回指向容器起始位置的常迭代器（const_iterator） 

cend 返回指向容器末尾位置的常迭代器 

=================Capacity================ 

size 返回有效元素个数 

max_size 返回 unordered_map 支持的最大元素个数 

empty 判断是否为空 

=================元素访问================= 

operator[] 访问元素 

at 访问元素 

=================元素修改================= 

insert 插入元素 

erase 删除元素 

swap 交换内容 

clear 清空内容 

emplace 构造及插入一个元素 

emplace_hint 按提示构造及插入一个元素 

================操作========================= 

find 通过给定主键查找元素 

count 返回匹配给定主键的元素的个数 

equal_range 返回值匹配给定搜索值的元素组成的范围 

================Buckets====================== 

bucket_count 返回槽（Bucket）数 

max_bucket_count 返回最大槽数 

bucket_size 返回槽大小 

bucket 返回元素所在槽的序号 

load_factor 返回载入因子，即一个元素槽（Bucket）的最大元素数 

max_load_factor 返回或设置最大载入因子 

rehash 设置槽数 

reserve 请求改变容器容量