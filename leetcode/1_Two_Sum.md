# Two Sum

---

> * 问题
> * 代码
> * map的使用方法
> * vector的使用方法

---

## 问题

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example :

Given nums = [ 2, 7, 11, 15 ],

​    target = 9,

​    Because nums[0] + nums[1] = 2 + 7 = 9,

​    return [ 0, 1 ].

## 代码

```c++
#include<iostream>
#include<vector>
#include<unordered_map>
    using namespace std;
class Solution {
public:
    // Solution();
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> res;
        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); ++i) {
            int t = target - nums[i];
            if (m.count(t) && m[t] != i) {
                res.push_back(i);
                res.push_back(m[t]);
                break;
            } 
        }
        return res;
    }
};
main(){

    Solution sl;
    vector<int> nums={2,7,11,15};
    vector < int > result;
    result=sl.twoSum(nums,9);
    cout<<"hello world"<<endl;
    for(int i=0;i<2 ;i++){
        cout<<result[i]<<endl;
    } 
    getchar();
    return 0;
}
```

## 具体方法

**map的使用**：

c++关于map的find和count的使用

使用count，返回的是被查找元素的个数。如果有，返回1；否则，返回0。注意，map中不存在相同元素，所以返回值只能是1或0。

使用find，返回的是被查找元素的位置，没有则返回map.end()。

std::map对应的数据结构是红黑树。红黑树是一种近似于平衡的二叉查找树，里面的数据是有序的。在红黑树上做查找、插入、删除操作的时间复杂度为O(logN)。而std::unordered_map对应哈希表，哈希表的特点就是查找效率高，时间复杂度为常数级别O(1)， 而额外空间复杂度则要高出许多。所以对于需要高效率查询的情况，使用std::unordered_map容器，但是std::unordered_map对于迭代器遍历效率并不高。而如果对内存大小比较敏感或者数据存储要求有序的话，则可以用std::map容器。

**vector的使用：**

在c++ 中，vector是一个十分有用的容器。

作用：它能够像容器一样存放各种类型的对象，简单地说，vector是一个能够存放任意类型的动态数组，能够增加和压缩数据。

vector在C++ 标准模板库中的部分内容，它是一个多功能的，能够操作多种数据结构和算法的模板类和函数库。

特别注意：

使用vector需要注意以下几点：

1、如果你要表示的向量长度较长（需要为向量内部保存很多数），容易导致内存泄漏，而且效率会很低；

2、Vector作为函数的参数或者返回值时，需要注意它的写法：

double

Distance(vector<int> &a, vector<int> &b) 其中的“&”绝对不能少！！！

实例：vector<int> test;

//建立一个vector，int为数组元素的数据类型，test为动态数组名

简单的使用方法如下：

vector<int> test; //建立一个vector

test.push_back(1);

test.push_back(2); //把1和2压入vector，这样test[0]就是1,test[1]就是2

自己见到的实例：

vector<vector<Point2f>> points; //定义一个二维数组

points[0].size(); //指第一行的列数

1 、基本操作

(1) 头文件 #include<vector>

(2)创建vector对象，vector<int> vec;

(3) 尾部插入数字：vec.push_back(a);

(4) 使用下标访问元素，cout << vec[0] << endl;记住下标是从0开始的。

(5)使用迭代器访问元素.

vector<int>::iterator it;

for (it = vec.begin(); it != vec.end(); it++)

​    cout << *it << endl;

(6) 插入元素： vec.insert(vec.begin() + i, a);在第i + 1个元素前面插入a;

(7) 删除元素： vec.erase(vec.begin() + 2);删除第3个元素vec.erase(vec.begin() + i, vec.end() + j);

删除区间[i, j - 1];区间从0开始

(8) 向量大小 : vec.size();

(9) 清空 : vec.clear();