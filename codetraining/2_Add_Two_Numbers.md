#Add Two Numbers

---

> * 问题
> * 代码
> * 主要思路

---

## 问题

给你2个链表，代表2个非负整数。链表中整数的每一位数字的存储是反序的，数组的每个节点都包含一个数字。

把2个非负整数相加，并且用一个链表返回。 输入 : (2->4->3) + (5->6->4)

输出 : 7->0->8

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution
{
  public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        
        ListNode *res=new ListNode(-1);
        ListNode *cur=res;
        int carry=0;
        while(l1||l2){
            int n1=l1? l1->val : 0;
            int n2=l2? l2->val : 0;
            int sum=n1+n2+carry;
            carry=sum/10;
            cur->next=new ListNode(sum%10);
            cur=cur->next;
            if(l1) l1=l1->next;
            if(l2) l2=l2->next;
        }
        if(carry) cur->next=new ListNode(1);
        return res->next;
    }
};
int main(){
    Solution sl;
    ListNode *l1=new ListNode(2);
    ListNode *l2=new ListNode(4);
    ListNode *l3=new ListNode(3);
    ListNode *l4=new ListNode(5);
    ListNode *l5=new ListNode(6);
    ListNode *l6=new ListNode(4);
    l1->next=l2;
    l2->next=l3;
    l4->next=l5;
    l5->next=l6;
    ListNode  *res=new ListNode(0);
    res->next=sl.addTwoNumbers(l1,l4);
    while(res->next!=NULL){
        res=res->next;
        if(res->next==NULL) cout<<res->val;
        else cout<<res->val<<"->";
    }
    getchar();
    return 0;
}
```

##主要思路

建立一个新链表，然后把输入的两个链表从头往后撸，每两个相加，添加一个新节点到新链表后面，

就是要处理下进位问题。还有就是最高位的进位问题要最后特殊处理一下。