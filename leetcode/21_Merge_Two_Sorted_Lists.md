#Merge Two Sorted Lists

---

> * 问题
> * 代码
> * 具体方法

---

## 问题

问题； 合并2个已经排序的链表，并且返回一个新的链表。这个新的链表应该由前面提到的2个链表的节点所组成。

## 代码

```c++
#include<iostream>
    using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
// 解法一：
class Solution1
{
  public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *dummy = new ListNode(-1), *cur = dummy;
        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                cur->next = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 ? l1 : l2;
        return dummy->next;
    }
};
// 解法二：
class Solution2
{
  public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        if (!l1)
            return l2;
        if (!l2)
            return l1;
        if (l1->val < l2->val)
        {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else
        {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
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
    do{
        cout << m->val << endl;
        m = m->next;
    }while(m);
}
int main(){
    Solution1 sl1;
    Solution2 sl2;
    ListNode *l1 = new ListNode(-1), *l2 =new ListNode(-1),*l3 = new ListNode(-1),*p=l3;

    createList(l1);
    // printList(l1);
    createList(l2);
    l3 = sl1.mergeTwoLists(l1,l2);
    printList(l3);
    getchar();
    return 0;
}
```

## 具体方法

c++ 中生成链表的操作：

构建链表节点结构体 

struct ListNode

{

​    int val;

​    ListNode *next;

​    ListNode(int x) : val(x), next(NULL) {}

};

// 创建链表

void createList(ListNode *pHead)

{

​    ListNode *p = pHead;

​    for (int i = 1; i < 10; ++i)

​    {

​        ListNode *pNewNode = new ListNode(-1);

​        pNewNode->val = i; // 将新节点的值赋值为i

​        pNewNode->next = NULL;

​        p->next = pNewNode; // 上一个节点指向这个新建立的节点

​        p = pNewNode;       // p节点指向这个新的节点

​    }

}

// 打印链表

void printList(ListNode *pHead)

{

​    ListNode *m = pHead->next;

​    do

​    {

​        cout << m->val << endl;

​        m = m->next;

​    } while (m);

}