#23 Merge k Sorted Lists

---

> * 问题
> * 代码
> * 思路

---

## 问题

合并k个有序链表

Merge k sorted linked lists and return it as one sorted list.Analyze and

describe its complexity.  

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution
{
  public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if(lists.empty()) return NULL;
        int n=lists.size();
        while(n>1){
            for(int i=0;i<n/2;i++){
                lists[i]=mergeTwoLists(lists[i],lists[n-i-1]);
            }
            n=(n+1)/2;
        }
        return lists.front();
    }
    ListNode *mergeTwoLists(ListNode *l1,ListNode *l2){
        if(l1==NULL) return l2;
        else if(l2==NULL) return l1;
        if(l1->val<=l2->val){
            l1->next=mergeTwoLists(l1->next,l2);
            return l1;
        }
        else{
            l2->next=mergeTwoLists(l1,l2->next);
            return l2;
        }
    }
};
int main()
{
    Solution sl;
    vector<int> v1={1,3,4};
    vector<int> v2={2,5,6};
    vector<int> v3={1,2,7};
    ListNode *l1=new ListNode(1);
    ListNode *p1=l1;
    ListNode *l2=new ListNode(1);
    ListNode *p2=l2;
    ListNode *l3=new ListNode(1);
    ListNode *p3=l3;
    for(int i=0;i<3;i++){
        l1->next=new ListNode(v1[i]);
        l1=l1->next;
        l2->next=new ListNode(v2[i]);
        l2=l2->next;
        l3->next=new ListNode(v3[i]);
        l3=l3->next;
    }
    vector<ListNode*> v4={p1,p2,p3};

    ListNode *res=sl.mergeKLists(v4);
    // cout<<res->val;
    while (res != NULL)
    {
        cout << res->val << endl;
        res = res->next;
    }
    cin.get();
    return 0;
}
```

## 思路

构造一个mergeTwoLists函数先两两比较k个有序数组，这里为了加速运算，从两边向中间开始比较，然后迭代下去。 mergeTwoLists中使用了递归的思想。