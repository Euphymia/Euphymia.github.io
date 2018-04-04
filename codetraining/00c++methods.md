# 关于一些C++方法的总结

---

> * 万能头文件
> * 链表的一些操作
> * 树的一些操作
> * memset()函数
> * sort()函数
> * max()函数
> * map的使用方法
> * vector的使用方法
> * stack的使用方法
> * 无视大小写判断字母是否相等的方法

---

### 万能头文件

include <bits/stdc++.h>

###链表的一些操作

```c++
// c++ 中生成链表的操作：

// 构建链表节点结构体 

struct ListNode

{

    int val;

    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}

};

// 创建链表

void createList(ListNode *pHead)

{

    ListNode *p = pHead;

    for (int i = 1; i < 10; ++i)

    {

        ListNode *pNewNode = new ListNode(-1);

        pNewNode->val = i; // 将新节点的值赋值为i

        pNewNode->next = NULL;

        p->next = pNewNode; // 上一个节点指向这个新建立的节点

        p = pNewNode;       // p节点指向这个新的节点

    }

}

// 打印链表

void printList(ListNode *pHead)

{

    ListNode *m = pHead->next;

    do

    {

        cout << m->val << endl;

        m = m->next;

    } while (m);

}
```

### 树的一些操作

```c++
定义树节点：
struct TreeNode
{
    int val;    
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL){};
};
 // 建立一个二叉搜索树
    TreeNode *t1=new TreeNode(8);
    TreeNode *t=t1;
    int j=0;
    int nums[]={3,15,1,5,0,2};
    for(int i=0;i<3;i++){
        TreeNode *t2=new TreeNode(nums[j++]);
        t1->left=t2;
        TreeNode *t3=new TreeNode(nums[j++]);
        t1->right=t3;
        t1=t1->left;
```

### memset()函数

memset：char型初始化函数

\#include <string.h>

函数原型：void *

memset(void *s, int ch, size_t n)

memset(结构体 / 数组名, 用于替换的ASCII码对应字符, 前n个字符);

memset(结构体/数组名 , "用于替换的字符" , 前n个字符 );

函数解释：将s中的前n个字节用ch替换并且返回s

函数作用：在一段内存块中填充某一个给定的值，常用于较大的对结构体和数组的清零操作。

### sort()函数

sort() 函数的使用方法：

Sort函数有三个参数：

（1）第一个是要排序的数组的起始地址。 

（2）第二个是结束的地址（最后一位要排序的地址）

（3）第三个参数是排序的方法，可以是从大到小也可是从小到大，还可以不写第三个参数，此时默认的排序方法是从小到大排序。 Sort函数使用模板 : Sort(start, end, , 排序方法)

​    升序：sort(begin, end, less<data - type>());

​    降序：sort(begin, end, greater<data - type>());

sort() 可以通过重写complare方法自定义比较方法。

例如

// complare方法定义在main函数之前。

bool complare(int a, int b)

{

​    // 从大到小排序

​    return a > b;

}

int a[10] = {9, 6, 3, 8, 5, 2, 7, 4, 1, 0};

sort(a, a + 10, complare); //在这里就不需要

### max()函数

```c++
// max()函数的使用方法：

int a=0;

a=max(3,8);

cout<<a;   // a=8
```

### map的使用方法

**map的使用**：

c++关于map的find和count的使用

使用count，返回的是被查找元素的个数。如果有，返回1；否则，返回0。注意，map中不存在相同元素，所以返回值只能是1或0。

使用find，返回的是被查找元素的位置，没有则返回map.end()。

std::map对应的数据结构是红黑树。红黑树是一种近似于平衡的二叉查找树，里面的数据是有序的。在红黑树上做查找、插入、删除操作的时间复杂度为O(logN)。而std::unordered_map对应哈希表，哈希表的特点就是查找效率高，时间复杂度为常数级别O(1)， 而额外空间复杂度则要高出许多。所以对于需要高效率查询的情况，使用std::unordered_map容器，但是std::unordered_map对于迭代器遍历效率并不高。而如果对内存大小比较敏感或者数据存储要求有序的话，则可以用std::map容器。

### vector的使用方法

vector的使用：

在c++ 中，vector是一个十分有用的容器。

作用：它能够像容器一样存放各种类型的对象，简单地说，vector是一个能够存放任意类型的动态数组，能够增加和压缩数据。vector在C++ 标准模板库中的部分内容，它是一个多功能的，能够操作多种数据结构和算法的模板类和函数库。特别注意：

**使用vector需要注意以下几点**：

1、如果你要表示的向量长度较长（需要为向量内部保存很多数），容易导致内存泄漏，而且效率会很低；

2、Vector作为函数的参数或者返回值时，需要注意它的写法：

double Distance(vector<int> &a, vector<int> &b) 其中的“&”绝对不能少！！！

简单的使用方法如下：

vector<int> test; //建立一个vector

test.push_back(1);

test.push_back(2); //把1和2压入vector，这样test[0]就是1,test[1]就是2

自己见到的实例：

vector<vector<Point2f>> points; //定义一个二维数组

points[0].size(); //指第一行的列数

**1 、基本操作**

1. vec.begin()//指向迭代器中第一个元素。   
2. vec.end()//指向迭代器中末端元素的下一个，指向一个不存在元素。          
3. vec.push_back(elem)     //在尾部加入一个数据。  
4. vec.pop_back()          //删除最后一个数据。  
5. vec.capacity()  //vector可用空间的大小。  
6. vec.size()//返回容器中数据个数。  
7. vec.empty() //判断容器是否为空。  
8. vec.front()     //传回第一个数据。  
9. vec.back()  //传回最后一个数据，不检查这个数据是否存在。  
10. vec.at(index)   //传回索引idx所指的数据，如果idx越界，抛出out_of_range。  
11. vec.clear() //移除容器中所有数据。  
12. vec.erase(iterator) //删除pos位置的数据，传回下一个数据的位置。  
13. vec.erase(begin,end)    //删除[beg,end)区间的数据，传回下一个数据的位置。注意：begin和end为iterator  
14. vec.insert(position,elem)   //在pos位置插入一个elem拷贝，传回新数据位置。  
15. vec.insert(position,n,elem) //在pos位置插入n个elem数据，无返回值。  
16. vec.insert(position,begin,end)  //在pos位置插入在[beg,end)区间的数据，无返回值。  

**vector的几种初始化方法：**

```c++
//初始化一个size为0的vector
vector<int> abc;
//初始化size,但每个元素值为默认值
vector<int> abc(10);    //初始化了10个默认值为0的元素
//初始化size,并且设置初始值
vector<int> cde(10，1);    //初始化了10个值为1的元素
int a[5] = {1,2,3,4,5};
//通过数组a的地址初始化，注意地址是从0到5（左闭右开区间）
vector<int> b(a, a+5);
vector<int> a(5,1);
//通过a初始化
vector<int> b(a);
//insert初始化方式将同类型的迭代器对应的始末区间（左闭右开区间）内的值插入到vector中
vector<int> a(6,6);
vecot<int> b;
//将a[0]~a[2]插入到b中，b.size()由0变为3
b.insert(b.begin(), a.begin(), a.begin() + 3);
```

### stack的使用方法

\#include <stack>

**stack的用法**

stack通过容器适配器来实现，是一种将特定的容器类作为其最底层的容器的类，它提供了一些特定的成员函数来访问自己的元素，元素只能在这个特定容器的后面，也就是栈的顶部，进行出栈和入栈操作。

最底层的容器可以是任意一种标准的容器模板类，或者是一些有明确目的的容器类，他们应该支持以下操作：

empty（判断是否为空）

size （返回栈的元素个数）

back （返回栈顶元素）

push （入栈）

pop （出栈）

### 无视大小写判断字母是否相等的方法

```c++
char ch1='A',ch2='a';
if((ch1+32-'a')%32!=(ch2+32-'a')%32) return false;
```